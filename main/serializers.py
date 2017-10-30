from rest_framework import serializers
from .models import Role, User, Document, Category


class RoleSerializer(serializers.ModelSerializer):
    """Role Serializer"""
    class Meta:
        model = Role
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
    """User Serializer"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email',
                  'full_name', 'password', 'about', 'role_id')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'id': {'read_only': True},
            'email': {'required': True}
        }

    def create(self, validated_data):
        user = User(**validated_data)

        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password:
            validated_data.pop('password')
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class DocumentSerializer(serializers.ModelSerializer):
    """Document Serializer"""
    user = serializers.ReadOnlyField()
    category = serializers.CharField(source='category.name', required=False)
    author_id = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Document
        fields = (
            'id', 'title', 'content', 'access', 'author_id', 'user',
            'category', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        if validated_data.get('category', None):
            try:
                validated_data['category'] = Category.objects.get(
                    name=validated_data['category']['name'])
            except:
                validated_data.pop('category')
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    def create(self, validated_data):
        if validated_data.get('category', None):
            try:
                validated_data['category'] = Category.objects.get(
                    name=validated_data['category']['name'])
            except:
                validated_data.pop('category')
        document = Document(**validated_data)
        document.save()
        return document


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

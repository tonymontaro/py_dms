from rest_framework import serializers
from .models import Role, User, Document


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name',)


class UserSerializer(serializers.ModelSerializer):
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
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.set_password(
            validated_data.get('password', instance.password))
        instance.save()
        return instance


class DocumentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    author_id = serializers.ReadOnlyField(source='author_identity')
    class Meta:
        model = Document
        fields = ('id', 'title', 'content', 'access', 'author_id', 'user',
                  'created_at', 'updated_at')

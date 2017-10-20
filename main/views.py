from django.http import HttpResponse
from rest_framework import generics, permissions, status
from .serializers import RoleSerializer, UserSerializer
from .models import Role, User
from .helpers import paginate

from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsProfileOwnerOrAdmin, IsAppAdmin
from rest_framework.authtoken.models import Token


def index(req):
    return HttpResponse('Hello and welcome to PyDMS.')


# Roles
class RoleList(generics.ListCreateAPIView):
    """List all ROLES or create a new Role"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()


class RoleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the http GET, PUT and DELETE requests"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated, IsAppAdmin)


# Users
class UserList(APIView):
    """List all users"""
    def get(self, req, format=None):
        total = User.objects.count()
        params = req.query_params
        limit = int(params.get('limit', 20))
        offset = int(params.get('offset', 0))

        users = User.objects.all()[offset:offset + limit]
        serializer = UserSerializer(users, many=True)
        meta_data = paginate(total, limit, offset)
        return Response({'rows': serializer.data, 'meta_data': meta_data})

    def post(self, req, format=None):
        serializer = UserSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            token = Token.objects.create(user=User.objects.get(username=req.data['username']))
            data['token'] = token.key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsProfileOwnerOrAdmin)

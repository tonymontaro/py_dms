from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import RoleSerializer, UserSerializer
from .models import Role
from django.contrib.auth.models import User


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
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


# Users
class UserList(generics.ListCreateAPIView):
    """List all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Retrieve a user"""
    queryset = User.objects.all()
    serializer_class = UserSerializer

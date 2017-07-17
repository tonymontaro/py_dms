from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from .serializers import RoleSerializer
from .models import Role


def index(req):
    return HttpResponse('Hello and welcome to PyDMS.')


# Role

class RoleListView(generics.ListAPIView):
    """Defines the ROLE list behavior"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleCreateView(generics.CreateAPIView):
    """Defines the ROLE create behavior"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class RoleDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles the http GET, PUT and DELETE requests"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

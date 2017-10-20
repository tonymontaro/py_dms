from rest_framework import permissions
from .models import Role


class IsProfileOwnerOrAdmin(permissions.BasePermission):
    """Allow only the owner of a profile"""
    def has_object_permission(self, request, view, obj):
        admin = Role.objects.get(name='admin')
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj or request.user.role_id == admin


class IsAppAdmin(permissions.BasePermission):
    """Allow only the admin"""
    def has_object_permission(self, request, view, obj):
        admin = Role.objects.get(name='admin')
        return request.user.role_id == admin

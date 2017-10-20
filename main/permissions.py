from rest_framework import permissions
from .models import Role


class IsProfileOwnerOrAdmin(permissions.BasePermission):
    """Allow only the owner of a profile"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        admin = Role.objects.get(pk=1)
        return request.user == obj or request.user.role_id == admin

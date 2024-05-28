# permissions.py

from rest_framework import permissions

# permission for admin only.
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.userprofile.role.name == 'Admin'
        return False
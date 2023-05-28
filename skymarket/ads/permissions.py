from rest_framework.permissions import BasePermission

from skymarket.users.managers import UserRoles


class AdPermission(BasePermission):
    message = 'you not allowed editing'

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        elif request.user.role == UserRoles.ADMIN.value[0]:  # пользователь является администратором
            return True
        return False
from rest_framework import permissions

from project.settings import TEACHER, PUPIL


class CustomPermissions(permissions.BasePermission):
    message = 'You don\'t have permission to access this resource.'

    def has_permission(self, request, view):
        if request.сustomuser.is_authenticated:
            if request.customuser.user_status == TEACHER or request.customuser.user.is_superuser:
                return True

            if request.customuser.user_status == PUPIL and request.method in permissions.SAFE_METHODS:
                return True

        return False

from rest_framework import permissions

from project.settings import TEACHER, PUPIL


class CustomPermissions(permissions.BasePermission):
    message = 'You don\'t have permission to access this resource.'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.user_status == TEACHER or request.user.is_superuser:
                return True
            elif request.user.user_status == PUPIL:
                return request.method in permissions.SAFE_METHODS

        return False

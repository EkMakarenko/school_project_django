# from rest_framework import permissions
#
# from project.settings import TEACHER, PUPIL
#
#
# class CustomPermissions(permissions.BasePermission):
#     message = 'You don\'t have permission to access this resource.'
#
#     def has_permission(self, request, view):
#         if request.user.user_status == TEACHER or request.user.user.is_superuser:
#             return True
#
#         if request.user.user_status == PUPIL and view.action == "GET":
#             return True
#
#         return False

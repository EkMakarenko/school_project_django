from django.contrib import admin

from user.models import User, Teacher, Pupil


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Users
    """
    list_display = ('id', 'get_full_name', 'gender', 'user_status', 'username')
    list_filter = ('user_status',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Teachers
    """
    list_display = ('id', 'get_full_name', 'group_manager', 'position', 'user')


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    """
    Schoolchild's
    """
    list_display = ('id', 'get_full_name', 'group', 'user')
    list_filter = ('group',)
    search_fields = ('get_full_name',)

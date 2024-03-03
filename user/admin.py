from django.contrib import admin

from user.models import Teacher, Pupil


# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    """
    Teachers
    """
    list_display = ('id', 'full_name', 'group_manager', 'position', 'user', 'get_phone', 'is_deleted')


@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    """
    Schoolchild's
    """
    list_display = ('id', 'full_name', 'group', 'user', 'is_deleted')
    list_filter = ('group',)
    search_fields = ('get_full_name',)

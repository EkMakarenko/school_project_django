from django.contrib import admin

from user.models import Teacher, Pupil


# Register your models here.

@admin.register(Pupil)
class PupilAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'gender', 'is_teacher')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'descriptions', 'is_teacher')
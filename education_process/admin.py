from django.contrib import admin

from education_process.models import Grade, RatingItemStatus, Score, Subject, PupilsGroup


# Register your models here.


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """
    Subjects
    """
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Grades
    """
    list_display = ('number', 'symbol')


@admin.register(RatingItemStatus)
class RatingItemStatusAdmin(admin.ModelAdmin):
    """
    Marks status.
    """
    list_display = ('name',)


@admin.register(PupilsGroup)
class PupilsGroupAdmin(admin.ModelAdmin):
    """
    Group of pupils
    """
    list_display = ('grade', 'create_group', 'updated', 'created',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """
    Marks
    """
    list_display = ('pupil', 'subject', 'score', 'created', 'updated', 'group')
    # list_filter = ('created', 'score', 'subject', 'group')



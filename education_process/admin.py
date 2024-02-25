from django.contrib import admin

from education_process.models import Grade, RatingItemStatus, Score, Subject


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
    list_display = ('grade',)


@admin.register(RatingItemStatus)
class RatingItemStatusAdmin(admin.ModelAdmin):
    """
    Marks status.
    """
    list_display = ('name',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """
    Marks
    """
    list_display = ('pupil', 'subject', 'score', 'created', 'group')



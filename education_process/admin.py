from django.contrib import admin

from education_process.models import Grade, RatingItemStatus, Lesson, Score, GroupSchoolchild


# Register your models here.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    """
    Уроки.
    """
    list_display = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    """
    Классы.
    """
    list_display = ('number', 'symbol')


@admin.register(RatingItemStatus)
class RatingItemStatusAdmin(admin.ModelAdmin):
    """
    Статусы оценок.
    """
    list_display = ('name',)


@admin.register(GroupSchoolchild)
class GroupSchoolchildAdmin(admin.ModelAdmin):
    """
    Оценки.
    """
    list_display = ('grade', 'create_group', 'updated', 'created',)


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    """
    Оценки.
    """
    list_display = ('schoolchild', 'lesson', 'score', 'created', 'updated', 'group')
    # list_filter = ('created', 'score', 'lesson', 'group')



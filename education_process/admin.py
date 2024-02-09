from django.contrib import admin

from education_process.models import Grade, Subject, Results


# Register your models here.


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade_at_school', 'branch')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name',)


@admin.register(Results)
class ResultsAdmin(admin.ModelAdmin):
    list_display = ('pupil', 'subject', 'marks', 'grade_at_school')



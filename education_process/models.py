from django.db import models
from django.urls import reverse_lazy

from project import settings
from project.settings import TEACHER, SCHOOLCHILD


# Create your models here.


class Lesson(models.Model):
    """
    Subject in the school curriculum
    """
    name = models.CharField('Name', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'List of school subjects'


class Grade(models.Model):
    """
    List of school subjects
    """
    number = models.SmallIntegerField('Grade')
    symbol = models.CharField('___ th grade', max_length=1)
    lessons = models.ManyToManyField(Lesson, related_name='grade', verbose_name='List of school subjects in grade')

    def __str__(self):
        return f'{self.number}{self.symbol}'

    class Meta:
        verbose_name = 'Grade'
        verbose_name_plural = 'List of grades'


class RatingItemStatus(models.Model):
    """
    Directory of mark statuses: current, quarterly, annual.
    """
    name = models.CharField('Mark status', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mark status'
        verbose_name_plural = 'List of marks status'


class GroupSchoolchild(models.Model):
    """
    Group of schoolchild
    """
    grade = models.OneToOneField(Grade, related_name='group', on_delete=models.CASCADE,
                                 verbose_name='Class name')
    create_group = models.DateField('Class creation date')
    updated = models.DateField('Update date', auto_now=True)
    created = models.DateField('Date of creation', auto_now_add=True)

    def __str__(self):
        return self.grade.__str__()

    def get_absolute_url(self):
        return reverse_lazy('group_schoolchild_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Group of schoolchild'
        verbose_name_plural = 'Groups of schoolchild'


class Score(models.Model):
    """
    Gradebook
    """
    SCORE_CHOICES = [
        (10, '10'),
        (9, '9'),
        (8, '8'),
        (7, '7'),
        (6, '6'),
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1')
    ]
    group = models.ForeignKey(GroupSchoolchild, on_delete=models.CASCADE, verbose_name='Class name')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Subject')
    schoolchild = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_schoolchild', on_delete=models.CASCADE,
                                  limit_choices_to={'user_status': SCHOOLCHILD}, verbose_name='Schoolchild')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_teacher', on_delete=models.SET_NULL,
                                null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Teacher')
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name='Mark')
    score_status = models.ForeignKey(RatingItemStatus, on_delete=models.CASCADE, verbose_name='Mark status')
    created = models.DateField(verbose_name='Date of creation')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    def __str__(self):
        return str(self.score)

    def get_absolute_url(self):
        return reverse_lazy('score_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Gradebook'
        verbose_name_plural = 'Marks'
        unique_together = ['schoolchild', 'lesson', 'created']

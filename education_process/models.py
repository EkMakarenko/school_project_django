from django.db import models

from project import settings
from project.settings import TEACHER, PUPIL


# Create your models here.


class Subject(models.Model):
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
    list of school subjects by grade
    """
    number = models.SmallIntegerField('Grade')
    symbol = models.CharField('___ th grade', max_length=1)
    subjects = models.ManyToManyField(Subject, related_name='grade', verbose_name='List of school subjects in grade')

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


class PupilsGroup(models.Model):
    """
    Group of pupils
    """
    grade = models.OneToOneField(Grade, related_name='Class', on_delete=models.CASCADE, verbose_name='Class name')
    create_group = models.DateField('Class creation date')
    updated = models.DateField('Update date', auto_now=True)
    created = models.DateField('Date of creation', auto_now_add=True)

    def __str__(self):
        return self.grade.__str__()

    class Meta:
        verbose_name = 'Class of pupil'
        verbose_name_plural = 'Class of pupils'


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
    group = models.ForeignKey(PupilsGroup, on_delete=models.CASCADE, verbose_name='Class name')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject')
    pupil = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_pupil', on_delete=models.CASCADE,
                                  limit_choices_to={'user_status': PUPIL}, verbose_name='Pupil')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_teacher', on_delete=models.SET_NULL,
                                null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Teacher')
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name='Mark')
    score_status = models.ForeignKey(RatingItemStatus, on_delete=models.CASCADE, verbose_name='Mark status')
    created = models.DateField(verbose_name='Date of creation')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update date')

    def __str__(self):
        return str(self.score)

    class Meta:
        verbose_name = 'Gradebook'
        verbose_name_plural = 'Marks'
        unique_together = ['pupil', 'subject', 'created']

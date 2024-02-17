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
    grade = models.CharField('___ th grade', max_length=20)

    def __str__(self):
        return self.grade

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

    def get_score_status(self):
        return self.name

    class Meta:
        verbose_name = 'Score status'
        verbose_name_plural = 'List of scores status'


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
    group = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Class name')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject')
    pupil = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_pupil', on_delete=models.CASCADE,
                                  limit_choices_to={'user_status': PUPIL}, verbose_name='Pupil')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='score_teacher', on_delete=models.SET_NULL,
                                null=True, limit_choices_to={'user_status': TEACHER}, verbose_name='Teacher')
    score = models.SmallIntegerField(choices=SCORE_CHOICES, verbose_name='Mark')
    score_status = models.ForeignKey(RatingItemStatus, on_delete=models.CASCADE, verbose_name='Mark status')
    created = models.DateField(verbose_name='Date of creation', blank=True, null=True)  #format='%Y-%m-%d', input_formats=['%Y-%m-%d', 'iso-8601']

    def __str__(self):
        return str(self.score)

    def get_subject(self):
        return f'{self.subject.name}'

    def get_pupil(self):
        return f'{self.pupil.last_name} {self.pupil.first_name} {self.pupil.middle_name}'

    def get_group(self):
        return f'{self.group.grade}'

    def get_score_status(self):
        return f'{self.score_status.name}'

    class Meta:
        verbose_name = 'Gradebook'
        verbose_name_plural = 'Marks'
        unique_together = ['pupil', 'subject', 'created']

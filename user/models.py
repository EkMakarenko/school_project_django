from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


from project import settings
from project.settings import TEACHER, PUPIL
from education_process.models import PupilsGroup, Subject

# Create your models here.


class User(AbstractUser):
    """
    User
    """
    GENDER_CHOICES = [('M', 'M'), ('F', 'F')]
    USER_STATUS_CHOICES = [(TEACHER, 'Teacher'), (PUPIL, 'Pupil')]
    username = models.CharField('Login', max_length=100, blank=True, null=True, unique=True)
    password = models.CharField('Password', blank=True)
    last_name = models.CharField('Last name', max_length=130, blank=True)
    first_name = models.CharField('First name', max_length=130, blank=True)
    middle_name = models.CharField('Middle name', max_length=130, blank=True)
    email = models.EmailField('Email', unique=True)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, max_length=1)
    birth_date = models.DateField('Birth_date', blank=True, null=True)
    description = models.TextField('Description', blank=True)
    user_status = models.CharField('User status', choices=USER_STATUS_CHOICES, max_length=15)
    # updated = models.DateField('Update date', auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    objects = UserManager()


class Teacher(models.Model):
    """
    Teacher
    """
    position = models.CharField('Position', max_length=100)
    group_manager = models.ForeignKey(PupilsGroup, related_name='teacher',
                                      verbose_name='Class teacher',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='teachers', verbose_name='Teach subject')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class Pupil(models.Model):
    """
    Pupil
    """
    group = models.ForeignKey(PupilsGroup, related_name='pupils', verbose_name='Studying a ___th grade',
                              on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='pupils', on_delete=models.CASCADE)

    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'Pupil'
        verbose_name_plural = 'Pupils'

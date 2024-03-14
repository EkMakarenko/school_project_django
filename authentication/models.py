from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from project.settings import TEACHER, PUPIL


class CustomUser(AbstractUser):
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
    phone = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, max_length=1)
    birth_date = models.DateField('Birth_date', blank=True, null=True)
    description = models.TextField('Description', blank=True)
    user_status = models.CharField('User status', choices=USER_STATUS_CHOICES, max_length=15)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return str(self.username)

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    objects = UserManager()

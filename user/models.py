from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.urls import reverse_lazy

from project import settings
from project.settings import TEACHER, SCHOOLCHILD


# Create your models here.


class User(AbstractUser):
    """
    User
    """
    GENDER_CHOICES = [('M', 'M'), ('F', 'F')]
    USER_STATUS_CHOICES = [(TEACHER, 'Teacher'), (SCHOOLCHILD, 'Schoolchild')]
    username = models.CharField('Login', max_length=30, blank=True, null=True, unique=True)
    password = models.CharField('Password', max_length=30, blank=True)
    last_name = models.CharField('Last name', max_length=130, blank=True)
    first_name = models.CharField('First name', max_length=130, blank=True)
    middle_name = models.CharField('Middle name', max_length=130, blank=True)
    email = models.EmailField('Email', unique=True)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, max_length=1)
    birth_date = models.DateField('Birth_date', blank=True, null=True)
    # photo = models.ImageField(upload_to='persons/', default='static/img/default-user.png', blank=True)
    description = models.TextField('Description', blank=True)
    user_status = models.CharField('User status', choices=USER_STATUS_CHOICES, max_length=15)
    # updated = models.DateField('Дата обновления', auto_now=True)

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
    group_manager = models.ForeignKey('education_process.GroupSchoolchild', related_name='teacher',
                                      verbose_name='Class teacher',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    lessons = models.ManyToManyField('education_process.Lesson', related_name='teachers', verbose_name='Teach lesson')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('teacher_detail', kwargs={'pk': self.user_id})

    @property
    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


class SchoolChild(models.Model):
    """
    Schoolchild
    """
    group = models.ForeignKey('education_process.GroupSchoolchild', related_name='schoolchilds', verbose_name='Studying a ___th grade',
                              on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='schoolchild', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy('schoolchild_detail', kwargs={'pk': self.user_id})

    def get_full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    class Meta:
        verbose_name = 'Schoolchild'
        verbose_name_plural = 'Schoolchilds'

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


from project import settings
from project.settings import TEACHER, PUPIL
from education_process.models import Subject, Grade
from user.managers import PersonManager, DeletedPersonManager


# Create your models here.

class Teacher(models.Model):
    """
    Teacher
    """
    position = models.CharField('Position', max_length=100)
    group_manager = models.ForeignKey(Grade, related_name='teacher',
                                      verbose_name='Class teacher',
                                      on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, related_name='subject', verbose_name='Teach subject', blank=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='teacher', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='teachers/', blank=True, null=True)
    is_deleted = models.BooleanField(null=False, default=False)

    @property
    def full_name(self):
        """
        Returns the full name of the user.
        """
        return f'{self.user.last_name} {self.user.first_name} {self.user.middle_name}'

    def get_description(self):
        """
        Returns the description of the user.
        """
        return {self.user.description}

    def get_phone(self):
        """
        Returns the phone number of the user.
        """
        return {self.user.phone}

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    objects = PersonManager()
    all_objects = models.Manager()
    deleted_objects = DeletedPersonManager()


class Pupil(models.Model):
    """
    Pupil
    """
    group = models.ForeignKey(Grade, related_name='pupils', verbose_name='Studying a ___th grade',
                              on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='pupils', on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=False, default=False)

    def __str__(self):
        """
        Returns a string representation of the group.
        """
        return self.group

    def __str__(self):
        """
        Returns a string representation of the full name.
        """
        return str(self.full_name())

    def full_name(self):
        """
        Returns the full name of the user.
        """
        return f'{self.user.last_name} {self.user.first_name} {self.user.middle_name}'

    class Meta:
        verbose_name = 'Pupil'
        verbose_name_plural = 'Pupils'

    objects = PersonManager()
    all_objects = models.Manager()
    deleted_objects = DeletedPersonManager()

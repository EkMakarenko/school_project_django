from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_photo = CloudinaryField('image')
    date_joined = models.DateTimeField(auto_now_add=True)

    def save_user(self):
        self.save()

    def update_user(self):
        self.update()

    def delete_user(self):
        self.delete()


class Pupil(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False)
    email = models.EmailField()
    gender = models.CharField(max_length=8, choices=select_gender)
    grade = models.ForeignKey(Grage, on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=500)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.user.username


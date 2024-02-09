from django.db import models

# Create your models here.


class Pupil(models.Model):
    select_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=8, choices=select_gender)
    is_teacher = models.BooleanField(default=False)


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256, null=True)
    phone = models.CharField(max_length=100)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    descriptions = models.CharField(max_length=500)
    is_teacher = models.BooleanField(default=True)

    def __str___(self):
        return self.phone

    def __str__(self):
        return self.first_name

#     def save_teacher(self):
#         self.save()
#
#     def update_teacher(self):
#         self.update()
#
#     def delete_teacher(self):
#         self.delete()

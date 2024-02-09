from django.db import models

from user.models import Pupil


# Create your models here.


class Grade(models.Model):
    select_grade = {
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    }

    select_branch = {
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    }
    grade_at_school = models.CharField(max_length=2, choices=select_grade)
    branch = models.CharField(max_length=2, choices=select_branch)

    def __str__(self):
        return self.grade_at_school

    def __str__(self):
        return self.branch


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return self.subject_name


class Results(models.Model):
    marks = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_at_school = models.ForeignKey(Grade, on_delete=models.CASCADE)
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.pupil.last_name


# class RegisterSubject(models.Model):
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     pupils = models.ForeignKey(Pupil, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.subject.subject_name

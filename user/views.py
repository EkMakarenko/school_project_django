from django.shortcuts import render
from rest_framework import viewsets

from education_process.serializers import SubjectCreateSerializer
from user.models import Teacher, Pupil, User
from user.serializers import PupilListSerializer, TeacherListSerializer, UserListSerializer, PupilCreateSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    serializer_classes = {
        'list': TeacherListSerializer,
        # 'create': TeacherCreateSerializer,
    }


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilListSerializer
    serializer_classes = {
        'list': PupilListSerializer,
        'create': PupilCreateSerializer,
    }

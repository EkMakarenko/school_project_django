from rest_framework import viewsets

from user.models import Teacher, Pupil, User
from user.serializers import PupilListSerializer, TeacherListSerializer, UserListSerializer, PupilCreateSerializer, \
    TeacherCreateSerializer, TeacherUpdateSerializer, TeacherRetrieveSerializer, PupilRetrieveSerializer, \
    PupilUpdateSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherListSerializer
    serializer_classes = {
        'list': TeacherListSerializer,
        'create': TeacherCreateSerializer,
        'retrieve': TeacherRetrieveSerializer,
        'update': TeacherUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    serializer_class = PupilListSerializer
    serializer_classes = {
        'list': PupilListSerializer,
        'create': PupilCreateSerializer,
        'retrieve': PupilRetrieveSerializer,
        'update': PupilUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

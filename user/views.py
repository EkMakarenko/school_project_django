from rest_framework import viewsets, filters

from user.models import Teacher, Pupil, User
from user.pagination import PupilPagination, TeacherPagination
from user.serializers import PupilListSerializer, TeacherListSerializer, UserListSerializer, PupilCreateSerializer, \
    TeacherCreateSerializer, TeacherUpdateSerializer, TeacherRetrieveSerializer, PupilRetrieveSerializer, \
    PupilUpdateSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    pagination_class = TeacherPagination
    ordering_fields = ('id', 'user__last_name', 'group_manager', 'position',)
    search_fields = ('user__last_name', 'user__first_name', 'group_manager', 'position',)
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
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    serializer_class = PupilListSerializer
    pagination_class = PupilPagination
    ordering_fields = ('id', 'user__last_name', 'group',)
    search_fields = ('user__last_name', 'user__first_name', 'group',)
    serializer_classes = {
        'list': PupilListSerializer,
        'create': PupilCreateSerializer,
        'retrieve': PupilRetrieveSerializer,
        'update': PupilUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

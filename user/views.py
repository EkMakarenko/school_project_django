from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from authentication.models import CustomUser
from user.serializers import (
    PupilListSerializer,
    TeacherListSerializer,
    PupilUpdateSerializer,
    PupilCreateSerializer,
    PupilRetrieveSerializer,
    TeacherCreateSerializer,
    TeacherUpdateSerializer,
    TeacherRetrieveSerializer,
    TeacherImageUpdateSerializer
)
from user.services import TeacherService
from user.models import Teacher, Pupil
from authentication.serializers import UserSerializer
from user.pagination import PupilPagination, TeacherPagination

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


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
        'update_image': TeacherImageUpdateSerializer,
    }

    def get_serializer_class(self):
        """
        Return the serializer class based on the current action.
        This method retrieves the serializer class based on the current action. It looks up the action in the
        `serializer_classes` dictionary and returns the corresponding serializer class. If the action is not found
        in the dictionary, it returns the default `serializer_class`.

        :return: Serializer class: The serializer class based on the current action.
        """
        return self.serializer_classes.get(self.action, self.serializer_class)

    @action(detail=True, methods=['patch'], url_path='update-image')
    def update_image(self, request, pk=None):
        """
        Update the image for a teacher object. This method updates the image for a teacher object based on the provided request data. It retrieves the teacher
        object, initializes a serializer based on the current action, updates the image using the TeacherService, performs
        the update, and returns a Response object with the updated data.

        :param request:Request object containing the data for the update.
        :param pk: Primary key of the teacher object to be updated (default is None).
        :return: Response object: Response containing the updated data.
        """
        teacher = self.get_object()
        serializer = self.serializer_classes.get(self.action, self.serializer_class)(teacher, request.data, partial=True)

        TeacherService.update_image(serializer=serializer, instance=teacher, request=request)

        self.perform_update(serializer)

        return Response(serializer.data)


class PupilViewSet(viewsets.ModelViewSet):
    queryset = Pupil.objects.all()
    filter_backends = (filters.OrderingFilter, filters.SearchFilter)
    serializer_class = PupilListSerializer
    pagination_class = PupilPagination
    ordering_fields = ('id', 'user__last_name', 'group',)
    search_fields = ('user__last_name', 'user__first_name', 'group',)
    # permission_classes = [IsAuthenticated,]
    serializer_classes = {
        'list': PupilListSerializer,
        'create': PupilCreateSerializer,
        'retrieve': PupilRetrieveSerializer,
        'update': PupilUpdateSerializer,
    }

    def get_serializer_class(self):
        """
        Return the serializer class based on the current action.
        This method retrieves the serializer class based on the current action. It looks up the action in the
        `serializer_classes` dictionary and returns the corresponding serializer class. If the action is not found
        in the dictionary, it returns the default `serializer_class`.

        :return: Serializer class: The serializer class based on the current action.
        """
        return self.serializer_classes.get(self.action, self.serializer_class)

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from authentication.models import CustomUser
from authentication.permissions import CustomPermissions
from authentication.serializers import UserSerializer, UserUpdateSerializer, UserCreateSerializer


class CustomUserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [CustomPermissions]
    serializer_classes = {
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
        'create': UserCreateSerializer,
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

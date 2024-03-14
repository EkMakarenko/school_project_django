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
        return self.serializer_classes.get(self.action, self.serializer_class)

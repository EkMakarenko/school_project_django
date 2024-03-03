from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from user.models import User
from authentication.serializers import UserSerializer, UserUpdateSerializer, UserCreateSerializer


class CustomUserViewSet(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    serializer_classes = {
        'update': UserUpdateSerializer,
        'partial_update': UserUpdateSerializer,
        'create': UserCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

from rest_framework import serializers
from djoser.serializers import UserSerializer as BaseUserSerializer
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

from authentication.models import CustomUser


class UserSerializer(BaseUserSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
            "last_name",
            "first_name",
            "middle_name",
            "email",
            "phone",
            "gender",
            "birth_date",
            "description",
            "user_status",
        )
        extra_kwargs = {
            'password': {'write_only': True},
            # 'username': {'write_only': True},
        }
        ref_name = 'CustomUserSerializer'


class UserCreateSerializer(BaseUserSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = (
            "username",
            "password",
            "email",
            "phone",
            "user_status",
        )
        ref_name = 'CustomUserCreateSerializer'


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all_'
        ref_name = 'CustomUserUpdateSerializer'

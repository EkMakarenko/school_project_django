from rest_framework import serializers

from education_process.serializers import SubjectListSerializer
from user.models import Pupil, Teacher, User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "last_name",
            "first_name",
            "middle_name",
            "email",
            "gender",
            "birth_date",
            "description",
            "user_status",
        )
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
        }


class TeacherListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserListSerializer.create(UserListSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(
            user=user,
            group_manager=validated_data.pop('group_manager'),
            position=validated_data.pop('position')
        )

        return teacher

    def get_user(self, obj):
        return obj.user.get_full_name


class TeacherCreateSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserListSerializer.create(UserListSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(
            user=user,
            group_manager=validated_data.pop('group_manager'),
            position=validated_data.pop('position')
        )

        return teacher


class TeacherUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherRetrieveSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class PupilListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)

    class Meta:
        model = Pupil
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.get_full_name


class PupilCreateSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)

    class Meta:
        model = Pupil
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserListSerializer.create(UserListSerializer(), validated_data=user_data)
        pupil, created = Pupil.objects.update_or_create(
            user=user,
            group=validated_data.pop('group')
        )

        return pupil


class PupilUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pupil
        fields = '__all__'


class PupilRetrieveSerializer(serializers.ModelSerializer):
    user = UserListSerializer()

    class Meta:
        model = Pupil
        fields = '__all__'

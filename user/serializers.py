from rest_framework import serializers

from user.models import Pupil, Teacher
from authentication.serializers import UserSerializer


class TeacherListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(
            user=user,
            group_manager=validated_data.pop('group_manager'),
            position=validated_data.pop('position')
        )

        return teacher

    def get_user(self, obj):
        return obj.user.get_full_name


class TeacherCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Teacher
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher, created = Teacher.objects.update_or_create(
            user=user,
            group_manager=validated_data.pop('group_manager'),
            position=validated_data.pop('position')
        )

        return teacher


class TeacherUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        exclude = ('image',)


class TeacherImageUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ('image', )


class TeacherRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Teacher
        fields = '__all__'


class PupilListSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Pupil
        fields = '__all__'

    def get_user_name(self, obj):
        return obj.user.get_full_name


class PupilCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Pupil
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
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
    user = UserSerializer()

    class Meta:
        model = Pupil
        fields = '__all__'

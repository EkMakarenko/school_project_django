from rest_framework import serializers

from education_process.models import Grade, RatingItemStatus, Score, Subject
from education_process.services import def_serializer


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name',)


class SubjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class SubjectUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class SubjectRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class GradeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('id', 'grade')


class GradeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('grade',)


class GradeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('grade',)


class GradeRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ('grade',)


class RatingItemStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('id', 'name',)


class RatingItemStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('name',)


class RatingItemStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('name',)


class RatingItemStatusRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('name',)


class ScoreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('id', 'get_pupil', 'get_subject', 'score', 'get_score_status', 'created', 'get_group')

    def_serializer()


class ScoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'score_status', 'created')


class ScoreUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'score_status', 'created')

    def_serializer()


class ScoreRetrieveSerializer(serializers.ModelSerializer):


    class Meta:
        model = Score
        fields = ('id', 'get_pupil', 'get_subject', 'score', 'get_score_status', 'created', 'get_group')

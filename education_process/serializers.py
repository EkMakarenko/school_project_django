from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from education_process.models import Grade, RatingItemStatus, Score, Subject


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'name',)


class SubjectCreateSerializer(serializers.ModelSerializer):
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


class RatingItemStatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('id', 'name',)


class RatingItemStatusCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('name',)


class ScoreListSerializer(serializers.ModelSerializer):
    # subject = serializers.SerializerMethodField()
    class Meta:
        model = Score
        fields = ('id', 'pupil', 'subject', 'score', 'created', 'group')

        # def get_subject(self, obj):
        #     return obj.subject.get_subject

        # @action(detail=True, methods=['get'], url_path='scores')
        # def scores(self, request, pk=None):
        #     pupil = self.get_object()
        #     scores = pupil.scores.all()
        #     serializer = ScoreListSerializer(scores, many=True)
        #     return Response(serializer.data)


class ScoreCreateSerializer(serializers.ModelSerializer):
    # subject = serializers.SerializerMethodField()
    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'created')

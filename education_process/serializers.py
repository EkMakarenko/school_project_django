from rest_framework import serializers

from education_process.models import Grade, RatingItemStatus, Score, Subject, PupilsGroup


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name',)


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('number', 'symbol')


class RatingItemStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingItemStatus
        fields = ('name',)


class PupilsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = PupilsGroup
        fields = ('grade', 'create_group', 'updated', 'created',)


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('pupil', 'subject', 'score', 'created', 'updated', 'group')
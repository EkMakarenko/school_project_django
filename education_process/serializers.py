from rest_framework import serializers

from education_process.models import Grade, RatingItemStatus, Score, Subject


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

        def get_subject(self, obj):
            return str(obj.subject.get_subject)

        def get_pupil(self, obj):
            return str(obj.pupil.get_pupil)

        def get_group(self, obj):
            return obj.grade.get_grade

        def get_score_status(self, obj):
            return obj.subject.get_score_status

        def get_group(self, obj):
            return obj.grade.get_grade


class ScoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'score_status', 'created')


class ScoreUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'score_status', 'created')


class ScoreRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Score
        fields = ('subject', 'group', 'pupil', 'score', 'score_status', 'created')

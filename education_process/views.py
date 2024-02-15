from rest_framework import viewsets

from education_process.models import Grade, RatingItemStatus, Score, Subject, PupilsGroup
from education_process.serializers import (GradeSerializer, RatingItemStatusSerializer,
                                           ScoreSerializer, SubjectSerializer, PupilsGroupSerializer)


# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # def get_serializer_class(self):
    #     return self.serializer_classes.get(self.action, self.serializer_class)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer


class RatingItemStatusViewSet(viewsets.ModelViewSet):
    queryset = RatingItemStatus.objects.all()
    serializer_class = RatingItemStatusSerializer


class PupilsGroupViewSet(viewsets.ModelViewSet):
    queryset = PupilsGroup.objects.all()
    serializer_class = PupilsGroupSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

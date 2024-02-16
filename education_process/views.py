from rest_framework import viewsets

from education_process.models import Grade, RatingItemStatus, Score, Subject
from education_process.serializers import (SubjectListSerializer, GradeListSerializer, ScoreListSerializer,
                                           RatingItemStatusListSerializer, SubjectCreateSerializer)


# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer
    serializer_classes = {
        'list': SubjectListSerializer,
        'create': SubjectCreateSerializer,
        # 'retrieve': SubjectRetrieveSerializer,
        # 'update': SubjectUpdateSerializer,
        # # 'partial_update': SubjectUpdateSerializer,
        # # 'recent_books': SubjectRecentBooksSerializer,
        # 'update_image': SubjectImageUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer


class RatingItemStatusViewSet(viewsets.ModelViewSet):
    queryset = RatingItemStatus.objects.all()
    serializer_class = RatingItemStatusListSerializer


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreListSerializer
    serializer_classes = {
        'list': SubjectListSerializer,
        'create': SubjectCreateSerializer,
    }

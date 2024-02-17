from rest_framework import viewsets, filters
from django_filters import rest_framework as django_filters

from education_process.filters import ScoreFilter
from education_process.models import Grade, RatingItemStatus, Score, Subject
from education_process.pagination import ScorePagination, RatingItemStatusPagination, SubjectPagination, GradePagination
from education_process.serializers import (SubjectListSerializer, GradeListSerializer, ScoreListSerializer,
                                           RatingItemStatusListSerializer, SubjectCreateSerializer,
                                           ScoreCreateSerializer, SubjectUpdateSerializer,
                                           RatingItemStatusCreateSerializer, RatingItemStatusUpdateSerializer,
                                           ScoreUpdateSerializer, ScoreRetrieveSerializer,
                                           RatingItemStatusRetrieveSerializer, SubjectRetrieveSerializer,
                                           GradeCreateSerializer, GradeRetrieveSerializer, GradeUpdateSerializer)


# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer
    pagination_class = SubjectPagination
    serializer_classes = {
        'list': SubjectListSerializer,
        'create': SubjectCreateSerializer,
        'retrieve': SubjectRetrieveSerializer,
        'update': SubjectUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer
    pagination_class = GradePagination
    serializer_classes = {
        'list': GradeListSerializer,
        'create': GradeCreateSerializer,
        'retrieve': GradeRetrieveSerializer,
        'update': GradeUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class RatingItemStatusViewSet(viewsets.ModelViewSet):
    queryset = RatingItemStatus.objects.all()
    serializer_class = RatingItemStatusListSerializer
    pagination_class = RatingItemStatusPagination
    serializer_classes = {
        'list': RatingItemStatusListSerializer,
        'create': RatingItemStatusCreateSerializer,
        'retrieve': RatingItemStatusRetrieveSerializer,
        'update': RatingItemStatusUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)


class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    filter_backends = (django_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = ScoreFilter
    pagination_class = ScorePagination
    ordering_fields = ('pupil', 'subject', 'score', 'created', 'group')
    serializer_class = ScoreListSerializer
    serializer_classes = {
        'list': ScoreListSerializer,
        'create': ScoreCreateSerializer,
        'retrieve': ScoreRetrieveSerializer,
        'update': ScoreUpdateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.serializer_class)

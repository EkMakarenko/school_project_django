from django_filters import rest_framework as django_filters

from user.models import Pupil
from education_process.models import Score, Grade


class ScoreFilter(django_filters.FilterSet):

    pupil = django_filters.ModelMultipleChoiceFilter(
        queryset=Pupil.objects.all(),
        field_name='pupil',
        to_field_name='id',
        lookup_expr='exact'
    )

    group = django_filters.ModelMultipleChoiceFilter(
        queryset=Grade.objects.all(),
        field_name='group',
        to_field_name='id',
        lookup_expr='exact'
    )

    class Meta:
        model = Score
        fields = ('pupil', 'group')

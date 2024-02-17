from rest_framework import pagination


class LessonPagination(pagination.PageNumberPagination):

    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20


class SubjectPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20


class GradePagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20


class RatingItemStatusPagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 20


class ScorePagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

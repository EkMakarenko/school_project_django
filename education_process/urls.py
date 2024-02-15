from django.urls import path
from rest_framework.routers import DefaultRouter

from education_process import views

router = DefaultRouter()
router.register(r'subjects', views.SubjectViewSet, basename='subject')
router.register(r'classes', views.GradeViewSet, basename='class')
router.register(r'markstatus', views.RatingItemStatusViewSet, basename='status')
router.register(r'pupils', views.PupilsGroupViewSet, basename='pupil')
router.register(r'score', views.ScoreViewSet, basename='score')

urlpatterns = router.urls

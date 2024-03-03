from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'teachers', views.TeacherViewSet, basename='teacher')
router.register(r'pupils', views.PupilViewSet, basename='pupil')

urlpatterns = router.urls

from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from authentication import views

app_name = 'authentication'
router = DefaultRouter()

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]



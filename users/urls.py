from django.urls import path
from .views import UsersModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"profiles", UsersModelViewSet, basename="profile")

urlpatterns = []

urlpatterns += router.urls

from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ReviewViewSet

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = []
urlpatterns += router.urls

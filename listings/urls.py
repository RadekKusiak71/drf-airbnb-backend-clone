from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ListingViewSets

router = DefaultRouter()
router.register(r"listings", ListingViewSets, basename="listing")

urlpatterns = []

urlpatterns += router.urls

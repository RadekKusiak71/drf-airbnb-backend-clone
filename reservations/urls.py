from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ReservationsViewSets

router = DefaultRouter()
router.register(r'reservations', ReservationsViewSets, basename='reservation')
urlpatterns = []


urlpatterns += router.urls

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightView

router = DefaultRouter()
router.register("flights", FlightView)

urlpatterns = [
]

urlpatterns += router.urls

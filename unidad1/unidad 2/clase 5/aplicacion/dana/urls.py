from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DanaViewSet

router = DefaultRouter()
router.register(r"dana", DanaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
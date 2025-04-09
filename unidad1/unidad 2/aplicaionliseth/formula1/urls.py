from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Formula1ViewSet

router = DefaultRouter()
router.register(r'formula1', Formula1ViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
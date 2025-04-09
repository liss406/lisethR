from django.shortcuts import render
from rest_framework import viewsets
from .models import Dana
from .serializers import DanaSerializers

class DanaViewSet(viewsets.ModelViewSet):
    queryset = Dana.objects.all()
    serializer_class = DanaSerializers


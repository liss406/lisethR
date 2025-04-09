from django.shortcuts import render
from rest_framework import viewsets
from .models import Formula1
from .serializers import Formula1Serializer

class Formula1ViewSet(viewsets.ModelViewSet):
    queryset = Formula1.objects.all()
    serializer_class = Formula1Serializer

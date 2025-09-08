from django.shortcuts import render
from rest_framework import viewsets
from factory.models import Factory
from factory.models import MCU
from .serializers import FactorySerializer
from .serializers import MCUSerializer

class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

class MCUViewSet(viewsets.ModelViewSet):
    queryset = MCU.objects.all()
    serializer_class = MCUSerializer
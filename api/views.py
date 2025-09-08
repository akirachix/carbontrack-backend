from django.shortcuts import render
from rest_framework import viewsets
from emissions.models import Emissions
from .serializers import EmissionsSerializer

class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all().order_by('-updated_at') 
    serializer_class = EmissionsSerializer

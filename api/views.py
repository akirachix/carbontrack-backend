from django.shortcuts import render
from rest_framework import viewsets
from emissions.models import Emissions
from .serializers import EmissionsSerializer
from factory.models import Factory
from factory.models import MCU
from .serializers import FactorySerializer
from .serializers import MCUSerializer
from django.shortcuts import render
from factory.models import EnergyEntry
from api.serializers import  EnergyEntrySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class EmissionsViewSet(viewsets.ModelViewSet):
    queryset = Emissions.objects.all().order_by('-updated_at') 
    serializer_class = EmissionsSerializer




class FactoryViewSet(viewsets.ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer

class MCUViewSet(viewsets.ModelViewSet):
    queryset = MCU.objects.all()
    serializer_class = MCUSerializer




class EnergyEntryViewSet(viewsets.ModelViewSet):
    queryset = EnergyEntry.objects.all()
    serializer_class = EnergyEntrySerializer
    @action(detail=False, methods=['get'])
    def summation_by_factory_and_date(self, request):
        factory_id = request.query_params.get('factory_id')
        date_str = request.query_params.get('date')
        date = parse_date(date_str) if date_str else timezone.now().date()
        co2 = EnergyEntry.get_co2_sum_by_factory_and_date(factory_id, date)
        tea_processed = EnergyEntry.get_tea_processed_sum_by_factory_and_date(factory_id, date)
        return Response({'factory_id': factory_id, 'date': date, 'co2_sum': co2, 'tea_processed_sum': tea_processed})
    

from .serializers import ComplianceSerializer
from rest_framework import viewsets
from emissions.models import Compliance
from django.utils import timezone
from rest_framework.decorators import action

class ComplianceViewSet(viewsets.ModelViewSet):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        compliance = self.get_object()
        date_str = request.data.get('date')
        date = parse_date(date_str) if date_str else timezone.now().date()
        compliance.update_compliance(date)
        serializer = self.get_serializer(compliance)
        return Response(serializer.data)

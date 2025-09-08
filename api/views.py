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
from django.shortcuts import render
from factory.models import EnergyEntry
from api.serializers import  EnergyEntrySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


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
    
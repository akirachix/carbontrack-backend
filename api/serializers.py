from rest_framework import serializers
from factory.models import Factory
from factory.models import MCU


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'

class MCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCU
        fields = '__all__'
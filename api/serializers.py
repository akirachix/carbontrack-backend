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

from factory.models import EnergyEntry

class EnergyEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyEntry
        fields = '__all__'
        read_only_fields = ['co2_equivalent']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        unit = instance.UNITS.get(instance.energy_type.lower(), '')
        amount = data.get('energy_amount')
        if amount is not None:
            data['energy_amount'] = f"{amount} {unit}"
        return data


from rest_framework import serializers
from emissions.models import Emissions
from factory.models import MCU



class EmissionsSerializer(serializers.ModelSerializer):
    device_id = serializers.CharField(write_only=True)  
    mcu = serializers.SerializerMethodField()            
    mcu_device_id = serializers.SerializerMethodField()   

    class Meta:
        model = Emissions
        fields = ('emissions_id', 'device_id', 'emission_rate', 'mcu', 'mcu_device_id', 'updated_at')

    def get_mcu(self, obj):
        return obj.mcu.mcu_id if obj.mcu else None

    def get_mcu_device_id(self, obj):
        return obj.mcu.mcu_id if obj.mcu else None

    def create(self, validated_data):
        device_id = validated_data.pop('device_id')
        try:
            mcu_instance = MCU.objects.get(mcu_id=device_id)
        except MCU.DoesNotExist:
            raise serializers.ValidationError({'device_id': 'MCU with this device_id does not exist.'})
        emission = Emissions.objects.create(mcu=mcu_instance, device_id=device_id, **validated_data)
        return emission

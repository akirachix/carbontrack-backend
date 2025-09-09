from rest_framework import serializers
from emissions.models import Emissions, Compliance
from factory.models import MCU, Factory, EnergyEntry

from users.models import User
import random
from django.core.cache import cache
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate


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


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'

class MCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCU
        fields = '__all__'



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


class ComplianceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compliance
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields =  [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
            "phone_number",
            "user_type",
            "factory",
            "profile_image",
            "created_at",
            "updated_at",
        ]
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def validate(self, data):
        user_type = data.get("user_type")
        factory = data.get("factory")
        if user_type == "factory" and not factory:
            raise serializers.ValidationError("Factory is required for Factory Managers.")
        if user_type == "manager" and factory:
            raise serializers.ValidationError("KTDA Managers cannot be linked to a factory.")
        return data



class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={'input_type': 'password'}
    )
    phone_number = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Phone number already registered.")]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Email already registered.")]
    )
    class Meta:
        model = User
        fields = [
            "first_name", "last_name", "phone_number", "email",
            "password", "user_type", "factory"
        ]
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)  
        user.save()
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        otp = random.randint(1000, 9999)
        cache.set(f"otp_{user.id}", otp, timeout=600)
        return value

        
class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    def validate(self, data):
        try:
            user = User.objects.get(email=data["email"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email")
        cached_otp = cache.get(f"otp_{user.id}")
        if not cached_otp or str(cached_otp) != str(data["otp"]):
            raise serializers.ValidationError("Invalid or expired OTP")
        return data


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)
    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return data
    def save(self, **kwargs):
        user = User.objects.get(email=self.validated_data["email"])
        user.set_password(self.validated_data["password"])
        user.save()
        cache.delete(f"otp_{user.id}")
        return user



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        if not user.is_active:
            raise serializers.ValidationError("This account is inactive.")
        data["user"] = user
        return data


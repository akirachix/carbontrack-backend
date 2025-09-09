from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from emissions.models import Emissions, Compliance
from .serializers import EmissionsSerializer, FactorySerializer, MCUSerializer, ComplianceSerializer
from api.serializers import  EnergyEntrySerializer
from factory.models import Factory, MCU, EnergyEntry
from rest_framework import viewsets, permissions, generics, status
from users.models import User
import random
from django.conf import settings
from django.core.cache import cache
from .serializers import (UserSerializer, SignupSerializer, LoginSerializer, ForgotPasswordSerializer, ResetPasswordSerializer, VerifyCodeSerializer)
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator



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







class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        access = AccessToken.for_user(user)
        return Response({
            "access": str(access),
            "user": {
                "id": user.id,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_type": user.user_type,
                "factory": user.factory.id if user.factory else None,
            }
        })



class ForgotPasswordView(generics.GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        user = User.objects.get(email=email)
        otp = cache.get(f"otp_{user.id}")
        send_mail(
            "Your OTP Code",
            f"Use this OTP to reset your password: {otp}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
        return Response({"message": "OTP sent to your email"})


class VerifyCodeView(generics.GenericAPIView):
    serializer_class = VerifyCodeSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OTP verified successfully"})


class ResetPasswordView(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Password has been reset successfully"})




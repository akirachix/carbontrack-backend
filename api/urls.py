from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, MCUViewSet, EnergyEntryViewSet, EmissionsViewSet, ComplianceViewSet
from .views import SignupView, LoginView, ForgotPasswordView, UserViewSet, ResetPasswordView, VerifyCodeView

router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet, basename='emissions')   
router.register(r'factories', FactoryViewSet)
router.register(r'mcus', MCUViewSet)
router.register(r'energy_entries', EnergyEntryViewSet)
router.register(r'compliance', ComplianceViewSet)
router.register(r'users', UserViewSet, basename = 'user')

urlpatterns = [
    path('api/', include(router.urls)),
    path("api/signup/", SignupView.as_view(), name="signup"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("api/verify-otp/", VerifyCodeView.as_view(), name = "verify-otp"),
    path("api/reset-password/", ResetPasswordView.as_view(), name = "reset-password"),
]




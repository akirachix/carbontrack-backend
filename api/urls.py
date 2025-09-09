
from django.urls import path, include
from .views import SignupView, LoginView, ForgotPasswordView, UserViewSet, ResetPasswordView, VerifyCodeView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename = 'user')

urlpatterns = [path('', include(router.urls)),
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("verify-otp/", VerifyCodeView.as_view(), name = "verify-otp"),
    path("reset-password/", ResetPasswordView.as_view(), name = "reset-password"),


]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, MCUViewSet, EnergyEntryViewSet, EmissionsViewSet, ComplianceViewSet

router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet, basename='emissions')   
router.register(r'factories', FactoryViewSet)
router.register(r'mcus', MCUViewSet)
router.register(r'energy_entries', EnergyEntryViewSet)
router.register(r'compliance', ComplianceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

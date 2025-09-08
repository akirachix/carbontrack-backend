from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmissionsViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, MCUViewSet
from .views import EnergyEntryViewSet



router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet, basename='emissions')   
router.register(r'factories', FactoryViewSet)
router.register(r'mcus', MCUViewSet)
router.register(r'energy_entries', EnergyEntryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/factories/',FactoryViewSet.as_view, name='factory-api'),
    path('api/mcus/',FactoryViewSet.as_view, name='factory-api'),

    ]




from rest_framework.routers import DefaultRouter
from api.views import ComplianceViewSet


router = DefaultRouter()
router.register(r'compliance', ComplianceViewSet)


urlpatterns=[
    path('api/', include(router.urls)),
]

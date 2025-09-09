from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmissionsViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, MCUViewSet
from .views import EnergyEntryViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet, basename='emissions')   
router.register(r'factories', FactoryViewSet)
router.register(r'mcus', MCUViewSet)
router.register(r'energy_entries', EnergyEntryViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/factories/',FactoryViewSet.as_view, name='factory-api'),
    path('api/mcus/',FactoryViewSet.as_view, name='factory-api'),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    ]





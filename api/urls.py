from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import FactoryViewSet, MCUViewSet


router = DefaultRouter()
router.register(r'factories', FactoryViewSet)
router.register(r'mcus', MCUViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/factories/',FactoryViewSet.as_view, name='factory-api'),
    path('api/mcus/',FactoryViewSet.as_view, name='factory-api'),

    ]

from .views import EnergyEntryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'energy_entries', EnergyEntryViewSet)

urlpatterns=[
     path('api/', include(router.urls))
]



from django.urls import path,include
from .views import EnergyEntryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'energy_entries', EnergyEntryViewSet)

urlpatterns=[
     path('api/', include(router.urls))
]


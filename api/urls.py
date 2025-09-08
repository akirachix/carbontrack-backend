from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EmissionsViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'emissions', EmissionsViewSet, basename='emissions')   
urlpatterns = [
    path('api/', include(router.urls)),
    
    ]



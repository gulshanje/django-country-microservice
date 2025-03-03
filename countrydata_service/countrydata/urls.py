from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryDataViewSet

router = DefaultRouter()
router.register(r'countrydata', CountryDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

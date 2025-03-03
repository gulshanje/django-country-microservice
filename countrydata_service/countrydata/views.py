from rest_framework import viewsets
from .models import CountryData
from .serializers import CountryDataSerializer

class CountryDataViewSet(viewsets.ModelViewSet):
    queryset = CountryData.objects.all()
    serializer_class = CountryDataSerializer

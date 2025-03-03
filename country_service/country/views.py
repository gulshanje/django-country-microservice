from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view

COUNTRYDATA_SERVICE_URL = "http://countrydata_service:8001/countrydata/"

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

@api_view(['GET'])
def get_country_details(request, code):
    response = requests.get(f"{COUNTRYDATA_SERVICE_URL}?country_code={code}")
    if response.status_code == 200:
        country_data = response.json()
        return Response(country_data)
    else:
        return Response({"error": "Country data not found"}, status=response.status_code)
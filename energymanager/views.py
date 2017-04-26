from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics, mixins
from .models import Address, Place, GSODWeatherStation
from .serializers import AddressSerializer, PlaceSerializer, GSODWeatherStationSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class GSODWeatherStationViewSet(viewsets.ModelViewSet):
    queryset = GSODWeatherStation.objects.all()
    serializer_class = GSODWeatherStationSerializer

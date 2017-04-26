from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics, mixins
from .models import Address, Place
from .serializers import AddressSerializer, PlaceSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

# class AddressList(generics.ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class AddressDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer
#
# class PlaceList(generics.ListCreateAPIView):
#     queryset = Place.objects.all()
#     serializer_class = PlaceSerializer
#
# class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Place.objects.all()
#     serializer_class = PlaceSerializer

from rest_framework import serializers

from .models import Address, Place, GSODWeatherStation

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        depth = 1

class GSODWeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GSODWeatherStation
        fields = '__all__'
        depth = 1

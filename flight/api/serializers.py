from rest_framework import serializers

from flight.models import Flight

class FlightModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Flight
        fields = [
            'id',
            'name',
            'location',
            'destination',
            'status',
            'dapart',
            'arrive',
            'price'
        ]

class FlightModelUpdateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Flight
        fields = [
            'location',
            'destination',
            'status',
            'dapart',
            'arrive',
            'price'
        ]
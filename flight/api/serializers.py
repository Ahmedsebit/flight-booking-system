from rest_framework import serializers

from flight.models import Flight

class FlightModelSerializer(serializers.ModelSerializer):


    class Meta:
        model = Flight
        fields = [
            'name',
            'location',
            'destination',
            'status',
            'date',
            'dapart',
            'arrive',
            'price'
        ]
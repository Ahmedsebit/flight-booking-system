from rest_framework import serializers
from django.urls import reverse_lazy
from seats.models import Seat

class SeatModelSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Seat
        fields = [
            "name",
        ]

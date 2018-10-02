from rest_framework import serializers
from customer_account.api.serializers import CustomerAccountModelSerializer
from flight.api.serializers import FlightModelSerializer
from seats.api.serializers import SeatModelSerializer

from bookings.models import Booking


class BookingModelSerializer(serializers.ModelSerializer):

    user = CustomerAccountModelSerializer()
    flight = FlightModelSerializer()
    seat = SeatModelSerializer()

    class Meta:
        model = Booking
        fields = (
            'ref',
            'user',
            "flight",
            "seat",
        )
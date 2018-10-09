from rest_framework import serializers
from customer_account.api.serializers import CustomerAccountModelSerializer
from flight.api.serializers import FlightModelSerializer
from seats.api.serializers import SeatModelSerializer
from user.api.serializers import UserSerializer
from user.models import CustomUser
from flight.models import Flight
from seats.models import Seat

from bookings.models import Booking


class BookingModelSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source='user',  queryset=CustomUser.objects.all())
    flight = FlightModelSerializer(read_only=True)
    flight_id = serializers.PrimaryKeyRelatedField(source='flight',  queryset=Flight.objects.all())
    seat = SeatModelSerializer(read_only=True)
    seat_id = serializers.PrimaryKeyRelatedField(source='seat',  queryset=Seat.objects.all())

    class Meta:
        model = Booking
        fields = (
            'ref',
            'user',
            'user_id',
            'flight',
            'flight_id',
            'seat',
            'seat_id'
        )
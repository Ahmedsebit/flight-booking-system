from rest_framework import serializers
from customer_account.api.serializers import CustomerAccountModelSerializer
from bookings.api.serializers import BookingModelSerializer
from bookings.models import Booking
from payment.models import Payment


class PaymentModelSerializer(serializers.ModelSerializer):

    booking = BookingModelSerializer(read_only=True)
    booking_id = serializers.PrimaryKeyRelatedField(source='booking',  queryset=Booking.objects.all())

    class Meta:
        model = Payment
        fields = (
            'ref',
            'booking',
            'booking_id',
            'payment'
        )
        

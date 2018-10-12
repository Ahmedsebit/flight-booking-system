from django import forms

from .models import Booking

class BookingModelForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'user',
            'flight',
            'seat',
        ]
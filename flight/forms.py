from django import forms

from .models import Flight

class FlightModelForm(forms.ModelForm):
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
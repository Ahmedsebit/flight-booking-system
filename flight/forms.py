from django import forms

from .models import Flight

class FlightModelForm(forms.ModelForm):
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
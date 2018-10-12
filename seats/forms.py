from django import forms

from .models import Seat

class SeatModelForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = [
            'name'
        ]
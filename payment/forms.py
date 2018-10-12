from django import forms

from .models import Payment

class PaymentModelForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'booking',
            'payment'
        ]
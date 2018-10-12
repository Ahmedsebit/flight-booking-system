from django import forms

from .models import CustomerAccount

class CustomerAccountModelForm(forms.ModelForm):
    class Meta:
        model = CustomerAccount
        fields = [
            "user",
            "bio",
            'birth_date',
            "country_of_residence",
            "travel_document_type",
            "travel_document_number",
            "phone",
            "address",
            "gender",
        ]
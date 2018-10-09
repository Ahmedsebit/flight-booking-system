from django import forms
from django.contrib.auth import get_user_model
# from .models import Profile

from customer_account.models import CustomerAccount

User = get_user_model()

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name', 'birth_date', 'nationality', 'country_of_residence', 'travel_document_type', 'travel_document_number', 'phone', 'address', 'gender')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

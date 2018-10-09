from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'birth_date', 'nationality', 'country_of_residence', 'travel_document_type', 'travel_document_number', 'phone', 'address', 'gender']

admin.site.register(CustomUser, CustomUserAdmin)
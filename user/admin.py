from django.contrib import admin

# Register your models here.

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('name', 'birth_date', 'nationality', 'country_of_residence', 'travel_document_type', 'travel_document_number', 'phone', 'address', 'gender','image')}),
)

class CustomUserAdmin(UserAdmin):
    aadd_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    fieldsets = UserAdmin.fieldsets + ADDITIONAL_USER_FIELDS

admin.site.register(CustomUser, CustomUserAdmin)
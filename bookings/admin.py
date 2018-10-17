from django.contrib import admin

# Register your models here.
from .forms import BookingModelForm
from .models import Booking

# admin.site.register(Tweet)

class BookingModelAdmin(admin.ModelAdmin):
    form = BookingModelForm
    # class meta:
    #     model = Flight
        

admin.site.register(Booking, BookingModelAdmin)
from django.contrib import admin

# Register your models here.
from .forms import FlightModelForm
from .models import Flight

# admin.site.register(Tweet)

class FlightModelAdmin(admin.ModelAdmin):
    form = FlightModelForm
    # class meta:
    #     model = Flight
        

admin.site.register(Flight, FlightModelAdmin)
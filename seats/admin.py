from django.contrib import admin

# Register your models here.
from .forms import SeatModelForm
from .models import Seat

# admin.site.register(Tweet)

class SeatModelAdmin(admin.ModelAdmin):
    form = SeatModelForm
    # class meta:
    #     model = Flight
        

admin.site.register(Seat, SeatModelAdmin)
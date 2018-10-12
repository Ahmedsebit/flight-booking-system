from django.contrib import admin

# Register your models here.
from .forms import PaymentModelForm
from .models import Payment

class PaymentModelAdmin(admin.ModelAdmin):
    form = PaymentModelForm
    # class meta:
    #     model = Flight
        

admin.site.register(Payment, PaymentModelAdmin)
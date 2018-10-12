from django.contrib import admin

# Register your models here.
from .forms import CustomerAccountModelForm
from .models import CustomerAccount

# admin.site.register(Tweet)

class CustomerAccountModelAdmin(admin.ModelAdmin):
    form = CustomerAccountModelForm
    # class meta:
    #     model = Tweet
        

admin.site.register(CustomerAccount, CustomerAccountModelAdmin)
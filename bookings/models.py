from django.db import models
from customer_account.models import CustomerAccount
from flight.models import Flight
from seats.models import Seat
# Create your models here.

from django.urls import reverse
from django.db import models

class Booking(models.Model):
    ref = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomerAccount, on_delete=models.CASCADE, null=False)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=False)
    seat =  models.ForeignKey(Seat, on_delete=models.CASCADE, null=False)

    def __str__ (self):
        return str(self.ref)

from django.core.exceptions import ValidationError
from bookings.models import Booking
# Create your models here.

from django.urls import reverse
from django.db import models

class Payment(models.Model):
    ref = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False)
    payment = models.CharField(max_length=30, unique=True)

    def __str__ (self):
        return str(self.ref)

    def get_absolute_url(self):
        return '/index'

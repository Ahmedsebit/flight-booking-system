from django.db import models
from bookings.models import Booking
# Create your models here.


class Payment(models.Model):
    ref = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, unique=True)
    payment = models.CharField(max_length=10, unique=True)

    def __str__ (self):
        return str(self.ref)

    # def get_absolute_url(self):
    #     return '/index'



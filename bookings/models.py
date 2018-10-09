from django.db import models
from customer_account.models import CustomerAccount
from user.models import CustomUser
from flight.models import Flight
from seats.models import Seat
# from account.models import CustomUser
# Create your models here.

from django.urls import reverse
from django.db import models

class Booking(models.Model):
    ref = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=False)
    seat =  models.ForeignKey(Seat, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('user','flight'),('seat','flight'))

    def clean(self):
        if self.flight.dapart <= timezone.now():
            raise ValidationError('This flight is unavailable')

    def clean(self):
        if self.flight.STATUS_CHOICES[2][0] == 'Canceled':
            raise ValidationError('This flight has been canceled')

    def __str__ (self):
        return str(self.ref)

    def get_absolute_url(self):
        return u'/payment/%d/' % self.ref

from django.db import models

# Create your models here.

from django.urls import reverse
from django.db import models

class Flight(models.Model):
    CONFIRMED = 1
    NOT_CONFIRMED = 2
    CANCELED = 3
    STATUS_CHOICES = (
        (CONFIRMED, 'Confirmed'),
        (NOT_CONFIRMED, 'Not confirmed'),
        (CANCELED, 'Canceled'),
    )
    name = models.CharField(max_length=140)
    location = models.CharField(max_length=140)
    destination = models.CharField(max_length=140)
    status =  models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=False, blank=True, default=1)
    date = models.DateTimeField(null=False)
    dapart = models.TimeField(null=False)
    arrive = models.TimeField(null=False)
    price = models.IntegerField(null=False, default=50000)

    def __str__ (self):
        return str(self.name)


from django.core.exceptions import ValidationError
from datetime import datetime, timedelta, time
from django.utils import timezone
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
    name = models.CharField(max_length=140, unique=True)
    location = models.CharField(max_length=140)
    destination = models.CharField(max_length=140)
    status =  models.PositiveSmallIntegerField(choices=STATUS_CHOICES, null=False, blank=True, default=1)
    dapart = models.DateTimeField(null=False)
    arrive = models.DateTimeField(null=False)
    price = models.IntegerField(null=False, default=50000)

    def clean(self):
        if self.dapart <= timezone.now():
            raise ValidationError('The date seems to be wrong')
        if self.dapart > self.arrive:
            raise ValidationError('Departure date cannot be later than the arrival date')
        if self.location == self.destination:
            raise ValidationError('The location and destination cannot be same')

    def __str__ (self):
        return str(self.name)


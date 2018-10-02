from django.db import models

# Create your models here.

from django.urls import reverse
from django.db import models

class Seat(models.Model):
    name = models.CharField(max_length=140)

    def __str__ (self):
        return str(self.name)


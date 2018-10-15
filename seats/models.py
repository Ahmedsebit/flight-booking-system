from django.db import models

# Create your models here.

class Seat(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__ (self):
        return str(self.name)


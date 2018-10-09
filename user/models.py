from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    MALE = 1
    FEMALE = 2
    ROLE_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    PASSPORT = 1
    NATIONAL_ID = 2
    ROLE_DOCUMENT = (
        (PASSPORT, 'Passport'),
        (NATIONAL_ID, 'National ID'),
    )

    name = models.CharField(blank=True, max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    country_of_residence = models.CharField(max_length=30, blank=True)
    travel_document_type = models.PositiveSmallIntegerField(choices=ROLE_DOCUMENT, null=True, blank=True)
    travel_document_number = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    gender = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.email
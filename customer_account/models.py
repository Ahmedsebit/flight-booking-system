from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomerAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    country_of_residence = models.CharField(max_length=30, blank=True)
    travel_document_type = models.CharField(max_length=30, blank=True)
    travel_document_number = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)

    def __str__ (self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def create_customer_account(sender, instance, created, **kwargs):
    if created:
        CustomerAccount.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customer_account(sender, instance, **kwargs):
    profile = User(user=instance)
    profile.save()

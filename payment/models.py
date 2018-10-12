from django.core.exceptions import ValidationError
from bookings.models import Booking
from django.db.models.signals import post_save

from flightbooking.mail import send_email, email_notification
from django.urls import reverse
from django.db import models
from bookings.models import Booking
# Create your models here.


class Payment(models.Model):
    ref = models.AutoField(primary_key=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=False, unique=True)
    payment = models.CharField(max_length=30, unique=True)

    def __str__ (self):
        return str(self.ref)

    def get_absolute_url(self):
        return '/index'


def post_save_payment(sender, instance, created, *args, **kwargs):
    booking = Booking.objects.get(ref=instance.booking.ref)
    email_subject = "Booking Done for flight "+booking.flight.name
    email_content = "Booking has been made for"
    print(booking.user.id)
    # send_email('booking@airtech.co.ke', booking.user.email, email_subject, email_content)
    email_notification()

post_save.connect(post_save_payment, sender=Payment)


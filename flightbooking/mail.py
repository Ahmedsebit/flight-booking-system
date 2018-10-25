import sendgrid
import os
from sendgrid.helpers.mail import *
from bookings.models import Booking
from datetime import datetime, timedelta, time
from django.utils import timezone


def send_email(email_to, email_subject, email_message):
    # os.environ.get('SENDGRID_API_KEY')
    sg = sendgrid.SendGridAPIClient(apikey='')
    from_email = Email("test@example.com")
    to_email = Email(email_to)
    subject = email_subject
    content = Content("text/plain", email_message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    

def email_notification():
    bookings = Booking.objects.all()
    subject = "Flight Reminder"
    message = "Message"
    for booking in bookings:
        dt = booking.flight.dapart - timezone.now()
        days_remaining = dt.days
        if booking.flight.dapart > timezone.now() and days_remaining <= 1:
            message = "This is a reminder for you flight: {}. Departure is on on {} at {}. Enjoy your flight, Fair Airlines.".format(booking.flight.name,booking.flight.dapart.isoformat(' ', 'seconds')[:10], booking.flight.dapart.isoformat(' ', 'seconds')[11:19])
            print(message)
            send_email(booking.user.email, subject, message)
            

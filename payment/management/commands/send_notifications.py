from django.core.management.base import BaseCommand
from flightbooking.mail import email_notification

import kronos

@kronos.register('1 * * * *')
class Command(BaseCommand):
    def handle(self, *args, **options):
        email_notification()
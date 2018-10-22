from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from rest_framework.test import APIRequestFactory
from  django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import force_authenticate
import json

from .models import Payment
from bookings.models import Booking
from flight.models import Flight
from seats.models import Seat
from user.models import CustomUser
# Create your tests here.


class PaymentModelTest(TestCase):

    def setUp(self):
        self.flight = Flight.objects.create(
                            name="Flight",
                            location='NRB',
                            destination="NRB",
                            status=1,
                            dapart='2010-11-01T00:00:00+05:00',
                            arrive='2018-11-02T00:00:00+05:00',
                            price=50000
                        )

        self.flight2 = Flight.objects.create(
                            name="Flight2",
                            location='NRB',
                            destination="NRB",
                            status=2,
                            dapart='2018-01-01T00:00:00+05:00',
                            arrive='2018-11-02T00:00:00+05:00',
                            price=50000
                        )

        self.flight3 = Flight.objects.create(
                            name="Flight3",
                            location='NRB',
                            destination="NRB",
                            status=2,
                            dapart='2018-01-01T00:00:00+05:00',
                            arrive='2018-11-02T00:00:00+05:00',
                            price=50000
                        )

        self.user = CustomUser.objects.create_superuser('test_username', 'test_username@example.com', 'da_password')
        self.seat = Seat.objects.create(name='1A')
        self.user2 = CustomUser.objects.create_user('test_username_2', 'test_username2@example.com', 'da_password')
        self.seat2 = Seat.objects.create(name='1A_2')
        self.booking = Booking.objects.create(flight=self.flight, seat=self.seat, user=self.user)
        self.booking2 = Booking.objects.create(flight=self.flight, seat=self.seat2, user=self.user2)
        self.booking3 = Booking.objects.create(flight=self.flight2, seat=self.seat2, user=self.user)
        self.booking4 = Booking.objects.create(flight=self.flight3, seat=self.seat, user=self.user)
        self.payment = Payment.objects.create(booking=self.booking3, payment="23456789")
        self.payment = Payment.objects.create(booking=self.booking4, payment="2345678990")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def create_payment(self, booking, payment):
        payment = Payment.objects.create(booking=booking, payment=payment)
        return payment

    def test_create_payment(self):
        payment = self.create_payment(self.booking, '900097879')
        self.assertTrue(isinstance(payment, Payment))
        self.assertEqual(payment.__str__(), str(payment.ref))
        
    def test_create_invalidMultipleayment(self):
        payment = self.create_payment(self.booking, '900097879')

        with self.assertRaises(IntegrityError):
            self.create_payment(self.booking2, '900097879')

    def test_create_invalidMyltipleBooking(self):
        payment = self.create_payment(self.booking, '900097879')

        with self.assertRaises(IntegrityError):
            payment = self.create_payment(self.booking2, '900097879')

    def test_get_payments_all_api(self):
        request = self.client.get('/api/payment/')
        self.assertEqual(request.status_code, 200)


    def test_get_customer_payment_api(self):
        request = self.client.get('/api/payment/customer/')
        self.assertEqual(request.status_code, 200)


    def test_get_payment_detail_api(self):
        request = self.client.get('/api/payment/'+str(self.flight.id)+'/')
        self.assertEqual(request.status_code, 200)

    def test_create_payment_api(self):
        request = self.client.post('/api/payment/create',
                                    json.dumps({
                                        'booking_id':2,
                                        'payment':'Testing'
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 201)


    def test_update_payment_api(self):
        request = self.client.put('/api/payment/'+str(self.booking.ref)+'/update',
                                    json.dumps({
                                        'booking_id':2,
                                        'payment':'Testing'
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 200)

    
    def test_get_payment_delete_api(self):
        request = self.client.delete('/api/payment/'+str(self.flight.id)+'/delete')
        self.assertEqual(request.status_code, 204)

        
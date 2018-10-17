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

from .models import Booking
from flight.models import Flight
from seats.models import Seat
from user.models import CustomUser
# Create your tests here.



User = get_user_model()

class BookingModelTest(TestCase):

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

        self.user = CustomUser.objects.create_user('test_username', 'test_username@example.com', 'da_password')
        self.seat = Seat.objects.create(name='1A')
        self.user2 = CustomUser.objects.create_user('test_username_2', 'test_username2@example.com', 'da_password')
        self.seat2 = Seat.objects.create(name='1A_2')
        self.user3 = CustomUser.objects.create_user('test_username_3', 'test_username3@example.com', 'da_password')
        self.seat3 = Seat.objects.create(name='1A_3')
        self.booking = Booking.objects.create(user=self.user3, flight=self.flight, seat=self.seat3)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def create_booking(self, flight, seat, user):
        booking = Booking.objects.create(flight=flight, seat=seat, user=user)
        return booking

    def test_create_booking(self):
        booking = self.create_booking(self.flight, self.seat, self.user)
        self.assertTrue(isinstance(booking, Booking))
        self.assertEqual(booking.__str__(), str(booking.ref))
        
    def test_create_invalidSeatt(self):
        booking = self.create_booking(self.flight, self.seat, self.user)

        with self.assertRaises(IntegrityError):
            self.create_booking(self.flight, self.seat, self.user2).full_clean()

    def test_create_invalidUser(self):
        booking = self.create_booking(self.flight, self.seat, self.user)

        with self.assertRaises(IntegrityError):
            self.create_booking(self.flight, self.seat2, self.user).full_clean()

    
    def test_get_bookings_all_api(self):
        request = self.client.get('/api/bookings/')
        self.assertEqual(request.status_code, 200)


    def test_get_bookings_all_api(self):
        request = self.client.get('/api/bookings/customer/')
        self.assertEqual(request.status_code, 200)


    def test_get_bookings_detail_api(self):
        request = self.client.get('/api/bookings/'+str(self.flight.id)+'/')
        self.assertEqual(request.status_code, 200)

    def test_create_booking_api(self):
        request = self.client.post('/api/bookings/create',
                                    json.dumps({
                                        'user_id':self.user.id,
                                        'flight_id':self.flight.id,
                                        'seat_id':self.seat.id
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 201)


    def test_update_booking_api(self):
        request = self.client.put('/api/bookings/'+str(self.booking.ref)+'/update',
                                    json.dumps({
                                        'user_id':self.user.id,
                                        'flight_id':self.flight.id,
                                        'seat_id':self.seat.id
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 200)


    def test_get_flight_detail_api(self):
        request = self.client.get('/api/bookings/'+str(self.flight.id)+'/')
        self.assertEqual(request.status_code, 200)

    
    def test_get_flight_delete_api(self):
        request = self.client.delete('/api/bookings/'+str(self.flight.id)+'/delete')
        self.assertEqual(request.status_code, 204)

        
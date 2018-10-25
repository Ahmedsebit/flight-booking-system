from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
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
from user.models import CustomUser
from .models import Flight

# Create your tests here.

from .models import Flight
from .forms import FlightModelForm

User = get_user_model()

class FlightModelTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_superuser(
            'test_username', 
            'test_username@example.com', 
            'da_password',
        )
        self.flight = Flight.objects.create(
                        name="FlightTest",
                        location = 'NRB',
                        destination = "DAR",
                        status = 1,
                        dapart = '2018-11-01T00:00:00+05:00',
                        arrive ='2018-11-02T00:00:00+05:00',
                        price = 50000
            )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def create_flight(self, name, location, destination, status, dapart, arrive, price):
        return Flight.objects.create(
                                name = name,
                                location = location,
                                destination = destination,
                                status =  status,
                                dapart = dapart,
                                arrive = arrive,
                                price = price
                                )


    def test_flight_creation(self):
        f = self.create_flight(
                            "Flight1",
                            'NRB',
                            "DAR",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        )

        data = {'name': f.name, 
                'location':f.location,
                'destination':f.destination,
                'status':f.status,
                'dapart':timezone.now(),
                'arrive':'2018-11-02T00:00:00+05:00',
                'price':f.price 
                }
        form = FlightModelForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(isinstance(f, Flight))
        self.assertTrue(f.name =="Flight1")
        self.assertEqual(f.__str__(), f.name)


    def test_creation_flight_nonunique_name(self):
        f = self.create_flight(
                            "Flight1",
                            'NRB',
                            "DAR",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        )
        with self.assertRaises(IntegrityError):
            self.create_flight(
                            "Flight1",
                            'NRB',
                            "DAR",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()

    
    def test_creation_flight_invalid_name(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight123456789",
                            'NRB',
                            "DAR",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()


    def test_creation_flight_invalid_location(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight",
                            'NRB123456789',
                            "DAR",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()

    
    def test_creation_flight_invalid_destination(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight",
                            'NRB',
                            "DAR123456789",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()


    def test_creation_flight_sdame_location_destination(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight",
                            'NRB',
                            "NRB",
                            1,
                            '2018-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()

    
    def test_creation_flight_Invalid_departure_date(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight",
                            'NRB',
                            "NRB",
                            1,
                            '2010-11-01T00:00:00+05:00',
                            '2018-11-02T00:00:00+05:00',
                            50000
                        ).full_clean()


    def test_creation_flight_Invalid_arrival_departure_date(self):
        with self.assertRaises(ValidationError):
            self.create_flight(
                            "Flight",
                            'NRB',
                            "NRB",
                            1,
                            '2010-11-02T00:00:00+05:00',
                            '2018-11-01T00:00:00+05:00',
                            50000
                        ).full_clean()


    def test_get_flight_all_api(self):
        request = self.client.get('/api/flight/')
        self.assertEqual(request.status_code, 200)

    
    def test_create_flight_api(self):
        request = self.client.post('/api/flight/create/',
                                    json.dumps({
                                        'name':"FlightT12",
                                        'location':'NRB',
                                        'destination':"DAR",
                                        'status':1,
                                        'dapart':'2018-11-01T00:00:00+05:00',
                                        'arrive':'2018-11-02T00:00:00+05:00',
                                        'price':50000
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 201)


    def test_get_flight_detail_api(self):
        request = self.client.get('/api/flight/'+str(self.flight.id)+'/')
        self.assertEqual(request.status_code, 200)

    
    def test_get_flight_delete_api(self):
        request = self.client.delete('/api/flight/'+str(self.flight.id)+'/delete/')
        self.assertEqual(request.status_code, 204)

    
    def test_get_flight_update_api(self):
        request = self.client.put('/api/flight/'+str(self.flight.id)+'/update/',
                                    json.dumps({
                                        'name':"FlightT12",
                                        'location':'NRB',
                                        'destination':"DAR",
                                        'status':1,
                                        'dapart':'2018-11-01T00:00:00+05:00',
                                        'arrive':'2018-11-02T00:00:00+05:00',
                                        'price':50000
                                        }),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 200)



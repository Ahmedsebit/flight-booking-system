from django.urls import reverse
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from  django.urls import reverse
from django.urls import reverse_lazy
from django.urls import resolve
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import force_authenticate
import json
from user.models import CustomUser
from .models import Seat
from .api.serializers import SeatModelSerializer
# Create your tests here.


class SeatModelTest(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = CustomUser.objects.create_superuser(
            'test_username', 
            'test_username@example.com', 
            'da_password',
        )
        self.seat = Seat.objects.create(name="1E")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def create_seat(self, name):
        return Seat.objects.create(name=name)

    def test_seat_creation(self):
        s = self.create_seat("1A")
        self.assertTrue(isinstance(s, Seat))
        self.assertTrue(s.name =='1A')
        self.assertEqual(s.__str__(), s.name)

    def test_creation_seat_invalid_name(self):
        with self.assertRaises(ValidationError):
            self.create_seat('1234567890A').full_clean()

    def test_creation_seat_nonunique_name(self):
        s = self.create_seat("1A")
        with self.assertRaises(IntegrityError):
            Seat.objects.create(name='1A').full_clean()

    def test_create_seat_api(self):
        request = self.client.post('/api/seats/create/',
                                    json.dumps({'name':'1A'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 201)

    def test_get_seat_all_api(self):
        request = self.client.get('/api/seats/')
        seats = Seat.objects.all()
        serializer = SeatModelSerializer(seats, many=True)
        self.assertEqual(request.data, serializer.data)
        self.assertEqual(request.status_code, 200)

    
    def test_get_seat_detail_api(self):
        request = self.client.get('/api/seats/'+str(self.seat.id)+'/detail/')
        seats = Seat.objects.get(pk=self.seat.id)
        serializer = SeatModelSerializer(seats)
        self.assertEqual(request.data, serializer.data)
        self.assertEqual(request.status_code, 200)

    def test_delete_seat_detail_api(self):
        request = self.client.delete('/api/seats/'+str(self.seat.id)+'/delete/')
        self.assertEqual(request.status_code, 204)

    def test_update_seat_api(self):
        request = self.client.put('/api/seats/'+str(self.seat.id)+'/update/',
                                    json.dumps({'name':'1A'}),
                                    content_type='application/json'
                                    )
        self.assertEqual(request.status_code, 200)



from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse_lazy
from django.test import TestCase
from django.contrib.auth.models import User
from django.core import management
from django.core.management import call_command
from django.utils.six import StringIO
from rest_framework.test import APIClient
from rest_framework import status
import json
from PIL import Image
from user.models import CustomUser
from rest_framework.authtoken.models import Token
import sys
import tempfile
from django.test import override_settings
from .models import CustomUser
from payment.management.commands.send_notifications import Command
# Create your tests here.

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from seats.models import Seat
from flight.models import Flight
class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        self.selenium.implicitly_wait(20)
        self.user = CustomUser.objects.create_user(
            'test_username', 
            'test_username@example.com', 
            'da_password',
        )
        self.seat = Seat.objects.create(name="1E")
        self.flight = Flight.objects.create(
                        name="FlightTest",
                        location = 'NRB',
                        destination = "DAR",
                        status = 1,
                        dapart = '2018-11-01T00:00:00+05:00',
                        arrive ='2018-11-02T00:00:00+05:00',
                        price = 50000
            )
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/users/signup/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        email = selenium.find_element_by_id('id_email')
        password1 = selenium.find_element_by_id('id_password1')
        password2 = selenium.find_element_by_id('id_password2')
        submit = selenium.find_element_by_name('register')

        #Fill the form with data
        username.send_keys('ahmedamedy')
        email.send_keys('staff@email.com')
        password1.send_keys('123456wordpass')
        password2.send_keys('123456wordpass')

        #submitting the form
        submit.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/user/login/')
        #find the form element
        username = selenium.find_element_by_id('id_username')
        password1 = selenium.find_element_by_id('id_password')
        submit = selenium.find_element_by_name('login')

        #Fill the form with data
        username.send_keys('ahmedamedy')
        password1.send_keys('123456wordpass')
        submit.send_keys(Keys.RETURN)

        selenium.get('http://127.0.0.1:8000/bookings/create')
        select1 = Select(selenium.find_element_by_id('id_user'))
        select1.select_by_value(str(self.user.id))
        select2 = Select(selenium.find_element_by_id('id_flight'))
        select2.select_by_value(str(self.flight.id))
        select3 = Select(selenium.find_element_by_id('id_seat'))
        select3.select_by_value(str(self.seat.id))
        submit = selenium.find_element_by_name('book')

        # user = CustomUser.objects.get(username='unary')

        #check the returned result
        # assert user is not None



def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image = image.convert('RGB')
    image.save(temp_file, 'jpeg')
    return temp_file


class UserModelTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            'test_username', 
            'test_username@example.com', 
            'da_password',
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_create_username(self):
        self.assertTrue(isinstance(self.user, CustomUser))


    def test_api_can_resister_a_user(self):
        response = self.client.get('/api/account/')
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_user(self):
        response = self.client.put('/api/account/'+str(self.user.id)+'/update/',
                                    json.dumps({
                                    "name": "Ahmed Yusuf",
                                    "nationality": "Kenya",
                                    "country_of_residence": "Kenya",
                                    "travel_document_type": 1,
                                    "travel_document_number": "A0987908",
                                    "phone": "0701874389",
                                    "address": "Test",
                                    "gender": 1}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 200) 


    def test_api_can_update_a_user__invalidphone(self):
        response = self.client.put('/api/account/'+str(self.user.id)+'/update/',
                                    json.dumps({
                                    "name": "Ahmed Yusuf",
                                    "nationality": "Kenya",
                                    "country_of_residence": "Kenya",
                                    "travel_document_type": 1,
                                    "travel_document_number": "A0987908",
                                    "phone": "07018743898909",
                                    "address": "Test",
                                    "gender": 1}),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, 400) 

    def test_email_notificatio(self):
        # management.call_command('send_notifications')
        out = StringIO()
        sys.stdout = out
        # call_command('send_notifications', stdout=out)
        # self.assertIn('', out.getvalue())
        command = Command()
        command.handle()
        self.assertIn('', out.getvalue())


    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_dummy_test(self):
        user_len = len(CustomUser.objects.all())
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        picture = CustomUser.objects.create(image=test_image.name)
        print ("It Worked!, ", picture.image)
        self.assertEqual(len(CustomUser.objects.all()), user_len+1)
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
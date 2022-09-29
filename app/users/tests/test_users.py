import base64
import json
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from users.models.users import User

PASSWORD = 'pAssw0rd!'


class AuthenticationTest(APITestCase):

    def test_user_can_sign_up(self):
        response = self.client.post(reverse('users:users-signup'), data={
            'username': 'useert',
            'email': 'juan@gmail.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': PASSWORD,
            'password_confirmation': PASSWORD,
        })
        user = User.objects.last()
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        #self.assertEqual(response.data['id'], user.id)
        self.assertEqual(response.data['username'], user.username)
        self.assertEqual(response.data['first_name'], user.first_name)
    
    def test_user_can_log_in(self): # new
        user = User.objects.create_user(
            username= 'useert',
            email= 'juan@gmail.com',
            first_name= 'Test',
            last_name= 'User',
            password= PASSWORD,
            )
        response = self.client.post(reverse('users:users-login'), data={
            'email': user.email,
            'password': PASSWORD,
        })

        access = response.data['access_token']
        print(response.data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(response.data['user']['username'], user.username)
        self.assertEqual(response.data['user']['first_name'], user.first_name)
        self.assertEqual(response.data['user']['last_name'], user.last_name)
        self.assertEqual(response.data['user']['email'], user.email)
        self.assertIsNotNone(access)
        
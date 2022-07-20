from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status


class UserRegisterTest(APITestCase):
	def setUp(self):
		self.test_user = User.objects.create_user(
			username='testuser',
			email='test@email.com',
			password='test_pa',
		)
		self.url = reverse('register')

	def test_create_user(self):
		data = {
			'username': 'user1',
			'email': 'email@email.com',
			'password': 'password',
		}
		response = self.client.post(self.url, data, format='json')

		self.assertEqual(User.objects.count(), 2)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['username'], data['username'])
		self.assertEqual(response.data['email'], data['email'])
		self.assertFalse('password' in response.data)

	def test_create_user_with_no_password(self):
		data = {
			'username': 'test_test',
			'email': 'email@email.com',
			'password': '',
		}
		response = self.client.post(self.url, data, format='json')

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(len(response.data['password']), 1)

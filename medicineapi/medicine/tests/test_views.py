from urllib import response
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.utils import timezone

from medicine.models import Company, Medicine

class APIViewTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.company = Company.objects.create(
            name='test_company',
            owner=self.user,
        )
        self.medicine = Medicine.objects.create(
            name='test_medicine',
            medicine_category='Pills',
            company=self.company,
            description='test_description',
            release_date=timezone.datetime(2020, 3, 10),
            expiration_date=timezone.datetime(2023, 5, 17),
        )
        client = APIClient()

    def test_company_list(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_company_detail(self):
        url = reverse('company-detail', args=['1'])
        response = self.client.get(url)
        print(response.data)
        print(url)
        self.assertEqual(response.status_code, 200)
from urllib import response

from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from faker import Faker
from rest_framework.test import APIClient, APITestCase
from test_plus.test import TestCase as PlusTestCase

from medicine.models import Company, Medicine

faker = Faker()

class APICompanyViewTest(APITestCase):
    """
    Testing CompanyViewSet action methods.
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='user',
            password='password',
        )
        self.company = Company.objects.create(
            name='test_company',
            owner=self.user,
        )
        self.test_user = User.objects.create_user(
            username='test_user',
            password='password',
        )
        self.company_data = {
        'name': 'test_company2',
        'owner': self.test_user
        }
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_company_list(self):
        url = reverse('company-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_company_list_create(self):
        self.client.force_authenticate(self.test_user)
        url = reverse('company-list')
        response = self.client.post(url, data=self.company_data)
        self.assertEqual(response.status_code, 201)

    def test_company_detail_retrieve(self):
        url = reverse('company-detail', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class APIMedicineViewTest(APITestCase):
    """
    Testing MedicineViewSet action methods.
    """
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
            description=faker.pystr(max_chars=50),
            release_date='2020-03-10',
            expiration_date='2023-05-17'
        )
        self.test_user = User.objects.create(
            username='test_user',
            password='password'
        )
        self.test_company = Company.objects.create(
            name='test_company2',
            owner=self.test_user,
        )
        self.medicine_data = {
            'name': 'test_medicine2',
            'medicine_category': 'Pills',
            'company': self.test_company,
            'description': faker.pystr(max_chars=50),
            'release_date': '2020-03-10',
            'expiration_date': '2023-05-17'
        }
        self.updated_medicine_data = {
            'name': 'test_medicine_updated',
            'medicine_category' :'Pills',
            'company': self.company,
            'description' :faker.pystr(max_chars=50),
            'release_date' :'2020-03-10',
            'expiration_date' :'2023-05-17'
        }
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_medicine_list(self):
        url = reverse('medicine-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_medicine_list_create(self):
    #     self.client.force_authenticate(self.test_user)
    #     url = reverse('medicine-list')
    #     response = self.client.post(url, data=self.medicine_data)
    #     self.assertEqual(response.status_code, 201)

    def test_medicine_detail_retrieve(self):
        url = reverse('medicine-detail', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_medicine_detail_patrial_update(self):
    #     url = reverse('medicine-detail', args=['1'])
    #     response = self.client.patch(url, data=self.updated_medicine_data)
    #     self.assertEqual(response.status_code, 200)

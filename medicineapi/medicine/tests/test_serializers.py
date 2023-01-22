from django.contrib.auth.models import User
from django.test.client import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.test import APIRequestFactory
from django.core.exceptions import ValidationError

from medicine.models import Company, Medicine
from medicine.serializers import CompanySerializer, MedicineSerializer
import faker

faker = faker.Faker()


class CompanySerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
            password='password',
        )
        self.company = Company.objects.create(
            name='test_company',
            owner=self.user,
        )
        self.auth_client = APIClient()
        self.auth_client.force_authenticate(user=self.user)
        self.request = APIRequestFactory()

    def test_company_serializer(self):
        serializer = CompanySerializer(
            instance=self.company, 
            context={'request': self.request.post('company-create')}
        )
        url = reverse('company-detail', args=['1'])
        response = self.auth_client.get(url)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

    
class MedicineSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user1',
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
            release_date='2020-03-10',
            expiration_date='2023-05-17',
        )
        self.invalid_medicine = Medicine.objects.create(
            name='invalid_medicine',
            medicine_category='Injection',
            company=self.company,
            description='test_description',
            release_date='2023-03-10',
            expiration_date='2020-05-17',
        )
        self.medicine_data = {
            'name': 'test_medicine2',
            'medicine_category': 'Pills',
            'company': self.company.pk,
            'description': 'test_description',
            'release_date': '2020-03-10',
            'expiration_date': '2023-05-17'
        }
        self.auth_client = APIClient()
        self.auth_client.force_authenticate(user=self.user)
        self.request = APIRequestFactory()

    def test_medicine_serializer(self):
        serializer = MedicineSerializer(
            instance=self.medicine,
            context={'request': self.request.post('medicine-create')}
        )
        invalid_serializer = MedicineSerializer(
            data=self.invalid_medicine,
            context={'request': self.request.post('medicine-create')}
        )
        url = reverse('medicine-detail', args=['1'])
        response = self.auth_client.get(url)

        self.assertEqual(invalid_serializer.is_valid(), False)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer.data, response.data)

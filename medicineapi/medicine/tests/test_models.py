from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from medicine.models import Company, Medicine


class ModelTest(TestCase):
    
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

    def test_company_model(self):
        """
        Company instances can be created and will be have right fields.
        """
        self.assertEqual(self.company.name, 'test_company')
        self.assertEqual(self.company.owner.username, 'user')
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(str(self.company), 'test_company')

    def test_medicine_model(self):
        """
        Medicine instances can be created and will be have right fields.
        """
        self.assertEqual(self.medicine.name, 'test_medicine')
        self.assertEqual(self.medicine.medicine_category, 'Pills')
        self.assertEqual(self.medicine.company.name, 'test_company')
        self.assertEqual(self.medicine.description, 'test_description')
        self.assertEqual(
            self.medicine.release_date, timezone.datetime(2020, 3, 10))
        self.assertEqual(
            self.medicine.expiration_date, timezone.datetime(2023, 5, 17))
        self.assertEqual(Medicine.objects.count(), 1)
        self.assertEqual(str(self.medicine), 'test_medicine')
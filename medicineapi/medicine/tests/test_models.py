from django.test import TestCase
from medicine.models import Company
from django.contrib.auth.models import User


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

    def test_company_name(self):
        self.assertEqual(self.company.name, 'test_company')

    def test_company_owner(self):
        self.assertEqual(self.company.owner.username, 'user')

    def test_company_slug(self):
        self.assertEqual(self.company.slug, 'test_company')
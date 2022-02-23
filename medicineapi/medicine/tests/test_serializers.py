# from multiprocessing import context
# from urllib import request
# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.utils import timezone
# from medicine.serializers import CompanySerializer, MedicineSerializer
# from rest_framework.request import Request

# from medicine.models import Company, Medicine


# class APISerializerTest(TestCase):
    
#     def setUp(self):
#         self.user1 = User.objects.create_user(
#             username='user1',
#             password='password',
#         )
#         self.user2 = User.objects.create_user(
#             username='user2',
#             password='password',
#         )
#         self.company1 = Company.objects.create(
#             name='test_company1',
#             owner=self.user1,
#         )
#         self.company2 = Company.objects.create(
#             name='test_company2',
#             owner=self.user2,
#         )
#         self.medicine = Medicine.objects.create(
#             name='test_medicine',
#             medicine_category='Pills',
#             company=self.company1,
#             description='test_description',
#             release_date=timezone.datetime(2020, 3, 10),
#             expiration_date=timezone.datetime(2023, 5, 17),
#         )

#     def test_company_serializer(self):
#         serializer_data = CompanySerializer(self.company1, self.company2, many=True)
#         expected_data = [
#             {
#                 'name': 'test_company1',
#                 'owner': 'user1',
#             },
#             {
#                 'name': 'test_company2',
#                 'owner': 'user2',
#             },
#         ]
#         self.assertEqual(serializer_data, expected_data)

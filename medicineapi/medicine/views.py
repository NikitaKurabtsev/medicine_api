from medicine.models import Company, Medicine
from serializers import CompanySerializer, MedicineSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

class CompanyViewSet(viewsets.ViewSet):
    # add authentication classes
    # add permission classes
    pass
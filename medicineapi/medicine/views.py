from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import CompanySerializer, MedicineSerializer

from medicine.models import Company, Medicine


class CompanyViewSet(viewsets.ViewSet):
    # add authentication classes
    # add permission classes
    pass
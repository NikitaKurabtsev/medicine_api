from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from medicine.permissions import IsOwnerOrReadOnly
from medicine.serializers import CompanySerializer, MedicineSerializer
from rest_framework import generics

from medicine.models import Company, Medicine


# class CompanyViewSet(viewsets.ViewSet):
#     # add authentication classes
#     # add permission classes
#     pass

class CompanyListCreate(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    name = 'company-list'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    name = 'company-detail'


class MedicineListCreate(generics.ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    name = 'medicine-list'


class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    name = 'medicine-detail'

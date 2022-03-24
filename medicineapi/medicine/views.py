from rest_framework import permissions, viewsets

from medicine.models import Company, Medicine
from medicine.permissions import IsOwnerOrReadOnly
from medicine.serializers import CompanySerializer, MedicineSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.select_related("company").all()
    serializer_class = MedicineSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly
    ]

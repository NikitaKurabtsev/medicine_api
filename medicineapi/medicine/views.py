from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from medicine.models import Company, Medicine
from medicine.permissions import IsOwnerOrReadOnly
from medicine.serializers import CompanySerializer, MedicineSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [SearchFilter]
    search_fields = ('name',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @method_decorator(cache_page(60*60*2))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.select_related('company').all()
    serializer_class = MedicineSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ('company', 'medicine_category')
    search_fields = ('name',)

    @method_decorator(cache_page(60*60*2))
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

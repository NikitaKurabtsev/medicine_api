from django.forms import ValidationError
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
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]


# class CompanyListCreate(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     name = 'company-list'

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#     name = 'company-detail'


# class MedicineListCreate(generics.ListCreateAPIView):
#     queryset = Medicine.objects.all()
#     serializer_class = MedicineSerializer
#     # permission_classes = (IsOwnerOrReadOnly,)
#     name = 'medicine-list'


# class MedicineDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Medicine.objects.all()
#     serializer_class = MedicineSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#     name = 'medicine-detail'


# api_view(['GET', 'POST'])
# def company_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer(companies, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = CompanySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(owner=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'POST'])
# @permission_classes((IsOwnerOrReadOnly,))
# def company_detail(request, pk):
#     try:
#         company = Company.objects.get(pk=pk)
#     except Company.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = CompanySerializer(company)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = CompanySerializer(company, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         company.delete()
#         return HttpResponse(status.HTTP_204_NO_CONTENT)

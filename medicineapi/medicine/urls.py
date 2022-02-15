from unicodedata import name
from django.urls import path
from medicine import views

urlpatterns = [
    path(
        'companies/', 
        views.CompanyListCreate.as_view(), 
        name=views.CompanyListCreate.name
    ),
    path(
        'companies/<int:pk>/', 
        views.CompanyDetail.as_view(), 
        name=views.CompanyDetail.name
    ),
    path(
        'medicines/', 
        views.MedicineListCreate.as_view(), 
        name=views.MedicineListCreate.name
    ),
    path(
        'medicines/<int:pk>/', 
        views.MedicineDetail.as_view(), 
        name=views.MedicineDetail.name
    ),
]
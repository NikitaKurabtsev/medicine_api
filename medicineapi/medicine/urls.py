from argparse import Namespace
from unicodedata import name

from django.db import router
from django.urls import path
from rest_framework import routers

from medicine import views

router = routers.DefaultRouter()

router.register(r'companies', views.CompanyViewSet)
router.register(r'medicines', views.MedicineViewSet)

urlpatterns = router.urls

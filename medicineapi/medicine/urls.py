from django.urls import include, path
from rest_framework import routers

from medicine import views

router = routers.DefaultRouter()

router.register(r'companies', views.CompanyViewSet)
router.register(r'medicines', views.MedicineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from authentication.views import UserCreate

urlpatterns = [
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"),
    path("register/", UserCreate.as_view(), name='register'),
]

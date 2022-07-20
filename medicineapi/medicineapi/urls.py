from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Medicine API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('medicine.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('authentication.urls')),
    path('swagger/', schema_view),
]

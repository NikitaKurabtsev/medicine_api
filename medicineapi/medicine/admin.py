from dataclasses import field
from django.contrib import admin
from .models import Company, Medicine

# Register your models here.
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Company._meta.get_fields()]

admin.site.register(Company)
admin.site.register(Medicine)
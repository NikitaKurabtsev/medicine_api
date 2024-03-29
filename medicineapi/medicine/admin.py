from django.contrib import admin

from .models import Company, Medicine


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'created')
    list_filter = ('name', 'created')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'medicine_category',
        'company', 'description',
        'expiration_date',
    )
    list_filter = ('name', 'medicine_category', 'company', 'description')
    search_fields = ('name', 'description')
    ordering = ('name', 'company')

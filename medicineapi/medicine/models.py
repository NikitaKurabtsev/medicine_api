from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Company(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique_for_date='created')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.owner


class MedicineCategory(models.Model):
    PILLS = 'Pills'
    LIQUIDS = 'Liquids'
    INJECTIONS = 'Injections'
    TYPE_CHOICES = (
        (PILLS, 'Pills'),
        (LIQUIDS, 'Liquids'),
        (INJECTIONS, 'Injections'),

    )
    medicine_category = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=False)

    def __str__(self):
        return self.medicine_category


class Medicine(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    medicine_category = models.ForeignKey(
        MedicineCategory, 
        related_name='medicine', 
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, 
        related_name='medicine', 
        on_delete=models.CASCADE
    )
    description = models.TextField(max_length=255, blank=False)
    expiration_date = models.DateField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

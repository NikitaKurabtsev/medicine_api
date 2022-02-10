from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique_for_date='created', blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)


class Medicine(models.Model):
    PILLS = 'Pills'
    LIQUIDS = 'Liquids'
    INJECTIONS = 'Injections'
    TYPE_CHOICES = (
        (PILLS, 'Pills'),
        (LIQUIDS, 'Liquids'),
        (INJECTIONS, 'Injections'),

    )
    name = models.CharField(max_length=50, unique=True)
    medicine_category = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=False)
    company = models.ForeignKey(
        Company, 
        related_name='medicine', 
        on_delete=models.CASCADE
    )
    description = models.TextField(max_length=255, blank=False)
    expiration_date = models.DateField(blank=False)
    slug = models.SlugField(max_length=255, unique_for_date='created', blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Medicine, self).save(*args, **kwargs)

from django.contrib.auth.models import User
from django.core.validators import validate_slug
from django.db import models
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, help_text="Название")
    owner = models.OneToOneField(User, on_delete=models.CASCADE, help_text="Владелец")
    created = models.DateTimeField(auto_now_add=True, help_text="дата регистрации компании")
    slug = models.SlugField(
        max_length=255, 
        unique_for_date="created", 
        blank=True, 
        validators=[validate_slug]
    )

    class Meta:
        ordering = ["-created"]
        verbose_name_plural = "Companies"

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Company, self).save(*args, **kwargs)


class Medicine(models.Model):
    PILLS = "Pills"
    LIQUIDS = "Liquids"
    INJECTIONS = "Injections"
    TYPE_CHOICES = (
        (PILLS, "Pills"),
        (LIQUIDS, "Liquids"),
        (INJECTIONS, "Injections"),
    )
    name = models.CharField(max_length=50, unique=True, help_text="Название")
    medicine_category = models.CharField(
        max_length=10, 
        choices=TYPE_CHOICES, 
        blank=False, 
        help_text="Тип лекарства",
    )
    company = models.ForeignKey(
        Company, 
        related_name="medicines", 
        on_delete=models.CASCADE,
        help_text="Компания"
    )
    description = models.TextField(max_length=255, blank=False, help_text="Описание")
    release_date = models.DateField(blank=False, help_text="Дата выпуска")
    expiration_date = models.DateField(blank=False, help_text="Дата окончания срока")
    slug = models.SlugField(
        max_length=255, 
        unique_for_date="created", 
        blank=True,
        validators=[validate_slug]
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):

        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Medicine, self).save(*args, **kwargs)

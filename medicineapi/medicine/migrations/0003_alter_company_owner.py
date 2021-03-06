# Generated by Django 4.0.2 on 2022-02-16 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0002_alter_medicine_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.OneToOneField(default=None, help_text='Владелец', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.0.6 on 2022-10-27 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0004_alter_company_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='medicine',
            name='slug',
        ),
    ]

# Generated by Django 3.2 on 2024-04-07 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Rental', '0003_auto_20240407_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='monthly_maintenance_cost',
        ),
    ]
# Generated by Django 4.0.4 on 2022-04-27 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0011_alter_converterlength_from_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='converterlength',
            name='unit_types_length',
        ),
        migrations.RemoveField(
            model_name='converterlength',
            name='unit_types_pressure',
        ),
    ]

# Generated by Django 4.0.4 on 2022-04-15 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='converter',
            old_name='unit_a',
            new_name='a_unit',
        ),
        migrations.RenameField(
            model_name='converter',
            old_name='unit_de',
            new_name='de_unit',
        ),
    ]

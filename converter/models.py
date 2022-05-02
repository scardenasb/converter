from django.db import models
from .tools import  length, pressure

# Create your models here.


TYPE_CHOICES = [
        ('Length', 'Length'),
        # ('Pressure', 'Pressure'),
        ]


UNIT_CHOICES_LENGTH = [
        ('millimeter', 'millimeter'),
        ('centimeter', 'centimeter'),
        ('meter', 'meter'),
        ('kilometer', 'kilometer'),
        ]


UNIT_CHOICES_PRESSURE = [
        ('psi', 'psi'),
        ('pascal', 'pascal'),
        ('atm', 'atmosphere'),
        ]

class ConverterLength(models.Model):

    to_unit = models.FloatField(unique=False, null=True, blank=True)
    from_unit = models.FloatField(unique=False, blank=False, null=False)
    types = models.CharField(unique=False, max_length=100, null=False, blank=True, default='Length')
    unit_types_from= models.CharField(unique=False, max_length=100, null=False, blank=True, default='millimeter')
    unit_types_to= models.CharField(unique=False, max_length=100, null=False, blank=True, default='millimeter')

    
    def __str__(self):
        return f'from {self.from_unit} to {self.to_unit}'

    def save(self, *args, **kwargs):
        if not self.to_unit:
            if self.types == "Length":
                self.to_unit = length(self)
            elif self.types == "Pressure":
                self.to_unit = pressure(self)
        super().save(*args, **kwargs)



    # def save(self, *args, **kwargs):
    #     if not self.to_unit:
    #         self.to_unit == parse(self)
    #     super().save(*args, **kwargs)

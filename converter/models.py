from django.db import models
from .tools import  length, pressure, volume

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, default=1)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UnitTo(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# TODO: Add new system options SI and AES (create a feature branch)
class ConverterLength(models.Model):
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, blank=True, null=True)
    from_unit = models.FloatField(unique=False, blank=True, null=True)
    to_unit = models.CharField(max_length=30, unique=False, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, blank=True, null=True)
    unit_to = models.ForeignKey(UnitTo, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'from {self.from_unit} to {self.to_unit}'

    def save(self, *args, **kwargs):

        if not self.to_unit:
            if self.type_id == 1:
                self.to_unit = length(self)

            elif self.type_id == 2:
                self.to_unit = pressure(self)

            elif self.type_id == 3:
                self.to_unit = volume(self)

        super().save(*args, **kwargs)

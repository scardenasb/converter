from django.contrib import admin
from .models import Unit, Type, UnitTo

# Register your models here.

admin.site.register(Unit)
admin.site.register(Type)
admin.site.register(UnitTo)

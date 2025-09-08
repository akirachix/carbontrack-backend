from django.contrib import admin

# Register your models here.

from .models import Factory, MCU, EnergyEntry
admin.site.register(Factory)
admin.site.register(MCU)
admin.site.register(EnergyEntry)
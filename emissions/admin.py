from django.contrib import admin

# Register your models here.
from .models import Emissions, Compliance
admin.site.register(Emissions)
admin.site.register(Compliance)

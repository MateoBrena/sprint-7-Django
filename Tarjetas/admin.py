from django.contrib import admin

# Register your models here.
from .models import Tarjeta, Marca_Tarjeta

admin.site.register(Marca_Tarjeta)
admin.site.register(Tarjeta)
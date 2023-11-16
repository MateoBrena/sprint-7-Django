from django.contrib import admin

# Register your models here.
from .models import Cliente, Tipo_Cliente

admin.site.register(Tipo_Cliente)
admin.site.register(Cliente)
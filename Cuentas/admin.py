from django.contrib import admin

# Register your models here.
from .models import Cuenta, Tipo_Cuenta

admin.site.register(Tipo_Cuenta)
admin.site.register(Cuenta)
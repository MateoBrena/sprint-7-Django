from django.db import models
from Sucursales.models import Sucursal
from django.contrib.auth.models import User

# Create your models here.

class Tipo_Cliente(models.Model):
    cliente_tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.cliente_tipo 

class Cliente(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    dob = models.CharField(max_length=100)
    branch = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo = models.ForeignKey(Tipo_Cliente, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.name + " " + self.surname
    


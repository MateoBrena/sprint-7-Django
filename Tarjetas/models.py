from django.db import models
from Clientes.models import Cliente
# Create your models here.

class Marca_Tarjeta(models.Model):
    marca = models.CharField(max_length=20)

    def __str__(self):
        return self.marca

class Tarjeta(models.Model):
    numero = models.CharField(max_length=19)
    cvv = models.IntegerField()
    fecha_otorgamiento = models.CharField(max_length=7)
    fecha_expiracion = models.CharField(max_length=7)
    tipo = models.CharField(max_length=7)
    marca = models.ForeignKey(Marca_Tarjeta, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


    def __str__(self):
        return "Tarjeta " + str(self.marca)
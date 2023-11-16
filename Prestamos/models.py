from django.db import models
from datetime import date
from Clientes.models import Cliente

# Create your models here.
class Prestamo(models.Model):
    tipo = models.CharField(max_length=30)
    fecha = models.DateField()
    monto = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
from django.db import models
from Clientes.models import Cliente

# Create your models here.
class Prestamo(models.Model):
    tipo = models.CharField(max_length=30)
    fecha = models.DateField()
    monto = models.IntegerField()
    estado = models.CharField(max_length=30)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo + ". Monto: $" + str(self.monto)
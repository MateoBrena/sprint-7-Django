from django.db import models
from Clientes.models import Cliente
# Create your models here.

class Tipo_Cuenta(models.Model):
    cuenta_tipo = models.CharField(max_length=30)

    def __str__(self):
        return self.cuenta_tipo

class Cuenta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    balance = models.IntegerField()
    iban = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo_Cuenta, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.tipo)
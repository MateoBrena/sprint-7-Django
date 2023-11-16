from django.db import models

# Create your models here.
class Sucursal(models.Model):
    nombre = models.CharField(max_length=50)
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre
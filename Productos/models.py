from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.UUIDField()
    nombre = models.CharField(max_length = 30)
    descripcion = models.Field(max_length = 60)
    precio = models.DecimalField(max_digits = 10, decimal places = 2)

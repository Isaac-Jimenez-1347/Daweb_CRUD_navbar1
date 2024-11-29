from django.db import models

# Create your models here.

class Productos(models.Model):
    id_producto=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=45)
    tipo=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=300)
    color=models.CharField(max_length=30)
    material=models.CharField(max_length=30)
    precio=models.PositiveIntegerField()
    id_sucursal=models.CharField(max_length=11)
    id_provedor=models.CharField(max_length=11)
    
    def __str__(self):
        return self.nombre
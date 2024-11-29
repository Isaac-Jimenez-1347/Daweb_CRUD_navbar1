from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_sucursal=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=45)
    ubicacion=models.CharField(max_length=30)
    horarios=models.CharField(max_length=300)
    email=models.CharField(max_length=30)
    celular=models.PositiveIntegerField()
    id_empleado=models.CharField(max_length=11)
    
    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.

class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=45)
    apellido_p=models.CharField(max_length=30)
    apellido_m=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    matricula=models.CharField(max_length=20)
    celular=models.PositiveIntegerField()
    puesto=models.CharField(max_length=30)
    salario=models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre
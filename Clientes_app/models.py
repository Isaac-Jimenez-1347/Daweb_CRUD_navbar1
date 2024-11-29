from django.db import models

# Create your models here.

class Clientes(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=45)
    apellido_p=models.CharField(max_length=30)
    apellido_m=models.CharField(max_length=30)
    fecha_nac = models.DateField(null=True, blank=True)
    email=models.CharField(max_length=20)
    celular=models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre
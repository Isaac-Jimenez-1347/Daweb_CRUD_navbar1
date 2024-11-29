from django.db import models

# Create your models here.

class Provedor(models.Model):
    id_provedor=models.CharField(primary_key=True,max_length=11)
    nombre_empresa=models.CharField(max_length=45)
    fecha = models.DateField(null=True, blank=True)
    horarios=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    celular=models.PositiveIntegerField()
    direccion=models.CharField(max_length=30)
    codigo_postal=models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre_empresa
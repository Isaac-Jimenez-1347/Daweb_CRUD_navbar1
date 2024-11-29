from django.db import models

# Create your models here.

class Pedidos(models.Model):
    id_pedido=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=45)
    fecha = models.DateField(null=True, blank=True)
    hora=models.CharField(max_length=30)
    id_producto=models.CharField(max_length=11)
    id_cliente=models.CharField(max_length=11)
    cantidad=models.PositiveIntegerField()
    id_trabajador=models.CharField(max_length=11)
    registro=models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre
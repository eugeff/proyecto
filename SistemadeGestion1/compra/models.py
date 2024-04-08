from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=20)
    dni = models.CharField(max_length=10,help_text='Sin puntos',primary_key=True)
    provincia=models.CharField(max_length=30)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre
    
    def get_absolut_url(self):
        return reversed('instancia particular',args=[str(self.nombre)])



class Producto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    precio = models.CharField(max_length=50)

    categorias= (
        ( 'electronica', 'electronica'),
        ('electrodomestico','electrodomestico'),
        ('hogar','hogar'),
        ('deporte','deportes')
    )
    categoria = models.CharField(max_length=30,choices=categorias)
    stockActual = models.IntegerField(default=0)
    proveedor = models.ForeignKey('Proveedor',on_delete=models.CASCADE)

    class Meta:
        ordering = ["categoria","nombre"]
    
    def __str__(self):
        return self.nombre
    
    def get_absolut_url(self):
        return reversed('producto-detail',args=[str(self.nombre)])
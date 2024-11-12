from django.db import models

# Create your models here.
class Productos(models.Model):
    codigo = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(blank=True)
    precio = models.PositiveIntegerField()
    cantidad = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Carpeta donde se guardarán las imágenes
#Cadigo para que el la tabla del administrados se vea el nombre del producto
    def __str__(self):
        return self.nombre

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    autor = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}"

class Proyectos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return f"{self.nombre}"

class Eventos(models.Model):
    nombre = models.CharField(max_length=100)
    organizador = models.CharField(max_length=100)
    fecha = models.DateField()  
    formato = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f"{self.nombre}"

class Merchandising(models.Model):
    nombre = models.CharField(max_length=100)
    valoraciones = models.IntegerField()
    descripcion = models.TextField()
    precio = models.FloatField()
    descuento = models.FloatField()
    delivery = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Merchandising"
        verbose_name_plural = "Merchandising"

    def __str__(self):
        return f"{self.nombre}"
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")   
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
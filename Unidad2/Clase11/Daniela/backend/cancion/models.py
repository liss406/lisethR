from django.db import models

class Cancion(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    duracion= models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

# Create your models here.

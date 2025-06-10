from django.db import models

class Libro(models.Model):
    
    titulo = models.CharField(max_length=200)
    genero = models.CharField(max_length=100)
    paginas = models.IntegerField()
    año_publicacion = models.IntegerField()

    def __str__(self):
        return self.titulo
    
# Create your models here.

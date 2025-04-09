from django.db import models

# Create your models here.

class Formula1 (models.Model):
    nombre = models.CharField(max_length=100)
    escuderia= models.CharField(max_length=100)
    rendimiento = models.IntegerField()
    genero =  models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
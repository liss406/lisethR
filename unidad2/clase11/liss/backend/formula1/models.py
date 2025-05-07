from django.db import models

class Formula1(models.Model):
    piloto = models.CharField(max_length=100)
    escuderia = models.CharField(max_length=100)
    rendimiento = models.FloatField()
    genero = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.piloto

# Create your models here.

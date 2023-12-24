from django.db import models

class NoticiaVideojuego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    # Otros campos que desees agregar a tu modelo

    def __str__(self):
        return self.titulo
from django.db import models

class NoticiaVideojuego(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()

    def __str__(self):
        return self.titulo
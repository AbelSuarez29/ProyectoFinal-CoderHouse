from django.db import models

class noticias(models.Model):
    noticia = models.CharField(max_length=100)
    informacion = models.CharField(max_length=200)

    def __str__(self):
        return self.noticia
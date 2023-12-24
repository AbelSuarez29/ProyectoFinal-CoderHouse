from django.db import models

class Usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    nacimiento = models.DateField(null= True, blank= True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


from django.db import models

class Eventos(models.Model):
	nombre = models.CharField(max_length=200)
	lugar = models.CharField(max_length=200)
	hora = models.DateTimeField()

class Usuarios(models.Model):
	nombre = models.CharField(max_length=200)
	correo = models.EmailField()
	eventos = models.ForeignKey(Eventos, blank=True, null=True)
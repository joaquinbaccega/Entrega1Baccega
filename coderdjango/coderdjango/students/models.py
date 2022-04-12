from django.db import models

class Documentacion(models.Model):
    dni = models.CharField(max_length=40)
    nacimiento = models.IntegerField()

class DatosPaciente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=40)
    nombre_doctor = models.CharField(max_length=40)
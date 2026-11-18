from django.db import models

# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    semestre = models.IntegerField()
    edad = models.IntegerField()
    materia = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    grupo = models.CharField(max_length=10)
    
    

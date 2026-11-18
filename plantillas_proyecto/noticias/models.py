from django.db import models

# Create your models here.
<<<<<<< HEAD

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    semestre = models.IntegerField()
    edad = models.IntegerField()
    materia = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    grupo = models.CharField(max_length=10)
    
    
=======
def Docente(models.Model): 
  nombre = models.CharField(max_length=100)
  apellidos = models.charField(max_lenght=100)
  edad = models.IntegerField()
  numero_ss = models.IntegerField()
  no_materias = models.IntegerField()
  no_alumnos = models.IntegerField()
  
>>>>>>> 16f87c6797e36f368fd7c288c9c037fdec969175

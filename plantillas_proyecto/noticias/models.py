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
    
class Docente(models.Model): 

  nombre = models.CharField(max_length=100)
  apellidos = models.charField(max_lenght=100)
  edad = models.IntegerField()
  numero_ss = models.IntegerField()
  no_materias = models.IntegerField()
  no_alumnos = models.IntegerField()

class Administrativo(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    numero_ss = models.IntegerField()
    puesto = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    salario = models.IntegerField()

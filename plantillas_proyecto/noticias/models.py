from django.db import models

# Create your models here.
def Docente(models.Model): 
  nombre = models.CharField(max_length=100)
  apellidos = models.charField(max_lenght=100)
  edad = models.IntegerField()
  numero_ss = models.IntegerField()
  no_materias = models.IntegerField()
  no_alumnos = models.IntegerField()
  
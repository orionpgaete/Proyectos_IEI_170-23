from django.db import models

# Create your models here.

class Proyectos(models.Model):
    fechaInicio=models.DateField()
    fechaTermino=models.DateField()
    nombre = models.CharField(max_length=50)
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()
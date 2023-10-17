from django.db import models

# Create your models here.
class empleados(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.CharField(max_length=70)
    fono = models.CharField(max_length=30)
    direccion = models.CharField(max_length=70)
    

from django.http import JsonResponse
from django.shortcuts import render
from proyecto_7_app import models

# Create your views here.

def empleadosview(request):
    emp = {
        'id' : 123,
        'nombre' : 'Juanito',
        'email' : 'juanito@gmail.com',
        'sueldo' : '11111000900'
    }
    return JsonResponse(emp)


def empleadosview_db(request):
    empleados = models.Empleados.objects.all()
    data = {'empleado' : list(empleados.values('nombre', 'sueldo'))}
    return JsonResponse(data)


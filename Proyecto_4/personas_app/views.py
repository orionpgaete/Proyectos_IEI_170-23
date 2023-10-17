from django.shortcuts import render
from personas_app.models import empleados

# Create your views here.

def trae_all_empleados(request):
    empleado = empleados.objects.all()
    data = {'emple' : empleado}
    return render (request, 'empleados.html', data)
from django.shortcuts import render
from proyecto_6_app.models import Proyectos

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoProyecto(request):
    proyectos = Proyectos.objects.all()
    data = {'proyecto': proyectos}
    return render(request, 'proyectos.html', data)


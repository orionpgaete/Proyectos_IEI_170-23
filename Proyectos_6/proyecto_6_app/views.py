from django.shortcuts import render, redirect
from proyecto_6_app.models import Proyectos
from proyecto_6_app.forms import FormProyecto

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoProyecto(request):
    proyectos = Proyectos.objects.all()
    data = {'proyecto': proyectos}
    return render(request, 'proyectos.html', data)

def agregarProyecto(request):
    form = FormProyecto()

    if (request.method == 'POST'):
        form = FormProyecto(request.POST)
        if (form.is_valid()):
            form.save()
        return index(request)
  
    data = {'form': form}
    return render (request, 'agregar.html', data)

def eliminarProyecto(request, IN_id):
    proyecto = Proyectos.objects.get(id = IN_id)
    proyecto.delete()
    return redirect('/proyectos')

def modificarProyecto(request, IN_id):
    proyecto = Proyectos.objects.get(id = IN_id)
    form = FormProyecto(instance=proyecto)

    if (request.method == 'POST'):
        form = FormProyecto(request.POST, instance=proyecto)
        if (form.is_valid()):
            form.save()
        return redirect('/proyectos')
  
    data = {'form': form}
    return render (request, 'agregar.html', data)
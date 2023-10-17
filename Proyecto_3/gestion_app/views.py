from django.shortcuts import render
from django.http import HttpResponse
from gestion_app.models import Productos

# Create your views here.

def busqueda(request):
    return render(request, "busca_producto.html")

def buscar(request):
    producto = request.GET["prd"]

    prod = Productos.objects.filter(nombre__icontains=producto)
    
    return render(request, "resultado.html", {"produc":prod, "query":producto})


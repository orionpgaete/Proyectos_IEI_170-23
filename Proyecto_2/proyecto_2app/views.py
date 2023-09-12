from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request, 'webproyecto_2/index.html')

def electronica(request):
    data ={"titulo":"Electronica"}
    return render(request, 'webproyecto_2/producto.html', data)

def juguete(request):
    data ={"titulo":"Juguetes"}
    return render(request, 'webproyecto_2/producto.html', data)

def ropa(request):
    data ={"titulo":"Ropa"}
    return render(request, 'webproyecto_2/producto.html', data)
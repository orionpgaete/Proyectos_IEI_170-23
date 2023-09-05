from django.shortcuts import render

# Create your views here.
def plantilla(request):
    return render(request, 'plantillaapp/plantilla.html')

def infousuario(request):
    data = {"id": "123", "nombre": "Pedro Gaete", "email": "pedro@gmail.com"}
    return render(request, 'plantillaapp/userinfotemplate.html', data)
from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    form = forms.registrousuario()
    data = {'forms': form}
    return render(request, 'index.html', data)
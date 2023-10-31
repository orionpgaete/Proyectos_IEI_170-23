# forms.py

from django import forms

class registrousuario(forms.Form):
    nombre = forms.CharField()
    fono = forms.CharField()
    email = forms.CharField()
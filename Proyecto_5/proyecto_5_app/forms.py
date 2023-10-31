# forms.py

from django import forms
from django.core import validators 

class registrousuario(forms.Form):

    ESTADOS = [('activo', 'ACTIVO'), ('inactivo', 'INACTIVO'), ('bloquedo', 'BLOQUEADO')]

    nombre = forms.CharField()
    fono = forms.CharField(required=False)
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    estado = forms.CharField(widget=forms.Select(choices=ESTADOS))

  #  def clean_nombre(self):
     #   inputnombre = self.cleaned_data['nombre']
     #   if inputnombre == 'Pablo':
   #         raise forms.ValidationError("No se aceptan mas PABLO!!!")
  #      return inputnombre
#
    def clean_nombre(self):
        inputnombre = self.cleaned_data['nombre']
        if len(inputnombre) > 20:
            raise forms.ValidationError("El largo maximo del nombre son 20 caracteres...")
        return inputnombre
    
    def clean_email(self):
        inputmail = self.cleaned_data['email']
        if inputmail.find('@') == -1:
            raise forms.ValidationError("El correo debe contener un @")
        return inputmail




    nombre.widget.attrs['class'] = 'form-control'
    fono.widget.attrs['class'] = 'form-control'
    email.widget.attrs['class'] = 'form-control'
    password.widget.attrs['class'] = 'form-control'
    estado.widget.attrs['class'] = 'form-select'
    
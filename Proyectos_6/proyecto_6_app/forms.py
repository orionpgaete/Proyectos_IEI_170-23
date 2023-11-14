from django import forms
from proyecto_6_app.models import Proyectos

class FormProyecto(forms.ModelForm):
    class Meta:
        model = Proyectos
        fields = '__all__'
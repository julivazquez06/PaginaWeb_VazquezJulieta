from django import forms
from .models import Profesores,Estudiantes,Cursos

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = "__all__"
        
class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = "__all__"
        
class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = "__all__"
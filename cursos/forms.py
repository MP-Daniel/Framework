from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'descripcion', 'intensidad_horaria', 'instructor', 'fecha_inicio', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descripción breve'}),
            'intensidad_horaria': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Horas (ej: 40)'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del instructor'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
        }

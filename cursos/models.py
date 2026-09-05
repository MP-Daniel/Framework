from django.db import models

class Curso(models.Model):
    ESTADOS = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('Completado', 'Completado'),
    ]
    
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    intensidad_horaria = models.PositiveIntegerField(help_text="En horas")
    instructor = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='Activo')

    def __str__(self):
        return self.nombre

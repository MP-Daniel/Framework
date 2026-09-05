import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_cursos.settings')
django.setup()

from cursos.models import Curso

cursos = [
    Curso(nombre='Introducción a Python', descripcion='Aprende los fundamentos de Python 3, estructuras de datos y funciones.', intensidad_horaria=20, instructor='Ana Martínez', fecha_inicio=date(2023, 10, 1), estado='Activo'),
    Curso(nombre='Desarrollo Web con Django', descripcion='Crea aplicaciones web robustas y escalables utilizando el framework Django.', intensidad_horaria=40, instructor='Carlos Gómez', fecha_inicio=date(2023, 11, 15), estado='Activo'),
    Curso(nombre='Bases de Datos SQL', descripcion='Domina el lenguaje SQL y el diseño de bases de datos relacionales.', intensidad_horaria=30, instructor='Laura Rodríguez', fecha_inicio=date(2023, 9, 10), estado='Completado'),
    Curso(nombre='Frontend con React', descripcion='Construye interfaces de usuario interactivas con React y JavaScript moderno.', intensidad_horaria=35, instructor='David López', fecha_inicio=date(2024, 1, 20), estado='Activo'),
    Curso(nombre='Machine Learning Básico', descripcion='Introducción a los algoritmos de aprendizaje automático con Scikit-Learn.', intensidad_horaria=50, instructor='Elena Silva', fecha_inicio=date(2023, 12, 5), estado='Inactivo')
]

Curso.objects.bulk_create(cursos)
print("Registros de prueba creados exitosamente.")

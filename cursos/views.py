from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso
from .forms import CursoForm

def curso_list(request):
    cursos = Curso.objects.all().order_by('-fecha_inicio')
    return render(request, 'cursos/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso registrado exitosamente.')
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'cursos/curso_form.html', {'form': form, 'accion': 'Registrar Curso'})

def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/curso_detail.html', {'curso': curso})

def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado exitosamente.')
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/curso_form.html', {'form': form, 'accion': 'Editar Curso'})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado exitosamente.')
        return redirect('curso_list')
    return render(request, 'cursos/curso_confirm_delete.html', {'curso': curso})

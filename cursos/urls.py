from django.urls import path
from . import views

urlpatterns = [
    path('', views.curso_list, name='curso_list'),
    path('curso/nuevo/', views.curso_create, name='curso_create'),
    path('curso/<int:pk>/', views.curso_detail, name='curso_detail'),
    path('curso/<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('curso/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),
]

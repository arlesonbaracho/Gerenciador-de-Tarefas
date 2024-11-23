from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Lista de tarefas
    path('create/', views.task_create, name='task_create'),  # Criar tarefa
    path('update/<int:pk>/', views.task_update, name='task_update'),  # Atualizar tarefa
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),  # Deletar tarefa
]

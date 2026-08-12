from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.view_task, name='view_task'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task/<int:task_id>/toggle/', views.toggle_task, name='toggle_task'),
]
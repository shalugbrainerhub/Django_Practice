
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('', views.viewTask, name='allTask'),
    path('add',views.addTaskView, name='addTask'),
    path('update/<int:task_id>', views.updateTaskView, name='updateTask'),
    path('delete/<int:task_id>', views.deleteTaskView, name='deleteTask')


]
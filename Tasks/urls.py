from django.urls import path
from . import views
"""
This file contains the url patterns for Task App 
urls for views are defined here

'/' : Home page of the app that contains the list of all the tasks 
'/add' : Add a new tasks
'/delete/<int:id>' : Delete a task 
'/update/<int:id>' : Update a task 
'/complete/<int:id>' : Mark a task as completed

"""
urlpatterns = [
    path('', views.ListTasksView.as_view(), name='Home'),
    path('add/', views.TaskCreateView.as_view(), name='Add'),
    path('update/<int:id>', views.TaskUpdateView.as_view(), name='Update'),
    path('delete/<int:id>', views.task_delete, name='Delete'),
    path('complete/<int:id>', views.complete_task, name='complete')

]

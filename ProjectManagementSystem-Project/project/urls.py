from django.urls import path
from .views import *

urlpatterns = [
    path('create_project/', CreateProject.as_view()),
    path('add_member/', AddMember.as_view()),
    path('add_task/<int:project_id>/', AddTask.as_view()),
    path('edit_task/<int:project_id>/<int:task_id>/', EditTask.as_view()),
]

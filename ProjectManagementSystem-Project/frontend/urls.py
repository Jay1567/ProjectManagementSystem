from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    
    path('projects', views.myProjects),
    path('addproject', views.newProject),

    path('members', views.members),
    path('addmember', views.addMember),

    path('tasks', views.myTasks),
    path('addtask', views.newTask),
    
    path('auth-signup', views.signup),
    path('dashboard', views.dashboard)
]

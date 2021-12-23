from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('forget-password/', views.reset_password),

    path('projects', views.myProjects),

    path('tasks', views.myTasks),
    path('addtask', views.newTask),
    
    path('auth-signup', views.signup),
    path('dashboard', views.dashboard),

    path('calendar', views.calendar),
    path('userprofile', views.updateProfile),

    path('bugreport', views.bugreport),
    path('bugdetail', views.bugdetail),


]

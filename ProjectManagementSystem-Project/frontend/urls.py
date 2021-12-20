from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('newproject', views.newProject),
    path('myprojects', views.myProjects),

]

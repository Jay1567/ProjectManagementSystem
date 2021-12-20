from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('newproject', views.newProject),
    path('myprojects', views.myProjects),
    path('auth-signup', views.signup),
    path('dashboard', views.dashboard),
    path('member', views.member),
]

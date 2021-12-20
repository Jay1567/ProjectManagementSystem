from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('auth-signup', views.signup),
    path('dashboard', views.dashboard)
]

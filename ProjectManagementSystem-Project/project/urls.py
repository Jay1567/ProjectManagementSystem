from django.urls import path
from .views import *

urlpatterns = [
    path('create_project/', CreateProject.as_view()),
    path('add_member/', AddMember.as_view()),
]

from .views import *
from django.urls import path

urlpatterns = [
    path('', sendInvitation.as_view()),
]

from rest_framework import generics
from .serializers import *


class CreateProject(generics.ListCreateAPIView):
    serializer_class = CreateProjectSerializer

    def get_queryset(self):
        user = self.request.user
        return user.projects.all()

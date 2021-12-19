from django.db.models import Q
from rest_framework import generics
from .serializers import *

class CreateProject(generics.ListCreateAPIView):
    serializer_class = CreateProjectSerializer

    def get_queryset(self):
        user = self.request.user.id
        return Project.objects.filter(Q(project_manager=user) | Q(team_members=user))
    
    
class AddMember(generics.CreateAPIView):
    serializer_class = AddMemberSerializer
    
    def get_queryset(self):
        user = self.request.user
        return user.Project_Assignees.all()


class AddTask(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        try:
            obj = Task.objects.get(id=project_id)
            if obj.project_manager == self.request.user.id:
                return Task.objects.filter(project_id=project_id)
            return Task.objects.filter(project_id=project_id, assignees=self.request.user.id)
        except Task.DoesNotExist: 
            raise generics.Http404


class EditTask(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    lookup_url_kwarg = ['task_id']

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        task_id = self.kwargs.get('task_id')
        try:
            return Task.objects.get(project_id=project_id, id=task_id)
        except Task.DoesNotExist:
            raise generics.Http404

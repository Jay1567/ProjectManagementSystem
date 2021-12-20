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


class ListTask(generics.ListCreateAPIView):
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


class ListDiscussionThread(generics.ListCreateAPIView):
    serializer_class = DiscussionThreadSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return DiscussionThread.objects.filter(project_id=project_id)


class EditDiscussionThread(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DiscussionThreadSerializer
    lookup_url_kwarg = ['thread_id']

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        thread = self.kwargs.get('thread_id')

        try:
            return DiscussionThread.objects.filter(project_id=project_id, id=thread)
        except DiscussionThread.DoesNotExist:
            raise generics.Http404


class GetCompleteDiscussionThread(generics.ListAPIView):
    serializer_class = DiscussionThreadNestedSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        thread = self.kwargs.get('thread_id')
        return DiscussionThread.objects.filter(project_id=project_id, id=thread)


class ListComments(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        thread = self.kwargs.get('thread_id')

        return Comment.objects.filter(thread=thread, thread__project_id=project_id)


class EditComment(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_url_kwarg = ['comment_id']

    def get_object(self):
        project_id = self.kwargs.get('project_id')
        thread = self.kwargs.get('thread_id')
        comment_id = self.kwargs.get('comment_id')

        try:
            return Comment.objects.filter(id=comment_id, thread=thread, thread__project_id=project_id)
        except Comment.DoesNotExist:
            raise generics.Http404

class GetMembers(generics.ListAPIView):
    serializer_class = GetMembersSerializer
    def get_queryset(self):
        user = self.request.user
        return Project_Assignees.objects.filter(project_id=self.kwargs.get('pk')) 
       

class EditMember(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EditMemberSerializer
    
    def get_object(self):
        project_id = self.kwargs.get('project_id')
        member_id=self.kwargs.get('member_id')
        try:
            obj = Project.objects.get(id = project_id)
            if obj.project_manager.id == self.request.user.id:
                return Project_Assignees.objects.get(project_id = project_id, member_id= member_id)
        except:
            raise generics.Http404


class CreateReport(generics.ListCreateAPIView):

    serializer_class = CreateReportSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        return Bug_Report.objects.filter(project_id=project_id) 
       

class EditReport(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = EditReportSerializer
    def get_object(self):
        project_id = self.kwargs.get('project_id')
        report_id = self.kwargs.get('report_id')
        user = self.request.user.id
        try:
            obj = Project.objects.get(id = project_id)
            
            if obj.project_manager.id == user:
                return Bug_Report.objects.get(project_id = project_id, id = report_id)
            elif Project_Assignees.objects.filter(project_id = project_id, member_id =user):
                return Bug_Report.objects.get(project_id = project_id, id = report_id)
        except:
            raise generics.Http404
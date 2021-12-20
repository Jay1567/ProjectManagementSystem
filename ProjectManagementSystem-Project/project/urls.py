from django.urls import path
from .views import *

urlpatterns = [
    path('create_project/', CreateProject.as_view()),
    path('add_member/<int:project_id>/', AddMember.as_view()),
    path('add_task/<int:project_id>/', ListTask.as_view()),
    path('edit_task/<int:project_id>/<int:task_id>/', EditTask.as_view()),
    path('list_discussion_thread/<int:project_id>/', ListDiscussionThread.as_view()),
    path('edit_discussion_thread/<int:project_id>/<int:thread_id>/', EditDiscussionThread.as_view()),
    path('get_complete_discussion_thread/<int:project_id>/<int:thread_id>/', GetCompleteDiscussionThread.as_view()),
    path('list_comments/<int:project_id>/<int:thread_id>/', ListComments.as_view()),
    path('edit_comments/<int:project_id>/<int:thread_id>/<int:comment_id>/', EditComment.as_view()),
    path('get_project_members/<int:pk>', GetMembers.as_view()),
    path('edit_project_member/<int:project_id>/<int:member_id>', EditMember.as_view()),
    path('create_bugreport/<int:project_id>/',CreateReport.as_view()),
    path('edit_bugreport/<int:project_id>/<int:report_id>/',EditReport.as_view())

]

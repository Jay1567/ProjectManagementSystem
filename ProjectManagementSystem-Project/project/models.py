from django.db import models
from django.db.models.fields.related_descriptors import create_forward_many_to_many_manager
from taggit.managers import TaggableManager
from django.conf import settings

from django.utils.timezone import now


class Project(models.Model):
    project_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                        related_name="projects")
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048, null=True, blank=True)
    tags = TaggableManager(blank=True)
    started_at = models.DateTimeField(auto_now_add=True, blank=True)
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Project_Assignees')

    def __str__(self):
        return self.name

class Project_Assignees(models.Model):
    role_type = (
        ("DEVOPS", "devops"),
        ("FRONTEND", "frontend"),
        ("BACKEND", "backend"),
        ("TESTER", "tester"),
    )
    member_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_members")
    role = models.CharField(max_length=256, choices=role_type)

    class Meta:
        unique_together =[['member_id', 'project_id']]


class Task(models.Model):
    task_status = (
        ("COMPLETED", "COMPLETED"),
        ("PENDING", "PENDING")
    )

    priority_type = (
        ("LOW", "LOW"),
        ("NORMAL", "NORMAL"),
        ("HIGH", "HIGH")
    )

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_tasks")
    deadline = models.DateTimeField()
    subject = models.CharField(max_length=2048)
    details = models.TextField(null=True, blank=True)
    status = models.CharField(choices=task_status, max_length=15, default="PENDING")
    priority = models.CharField(choices=priority_type, max_length=15, default="NORMAL")
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="task_assignee")
    assign_date = models.DateTimeField(default=now)
    
    # TODO: Add Multi file upload


class DiscussionThread(models.Model):
    thread_status = (
        ('ACTIVE', 'ACTIVE'),
        ('CLOSE', 'CLOSE')
    )

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=512)
    body = models.TextField(max_length=10000)
    tags = TaggableManager(blank=True)
    created_at = models.DateTimeField(default=now)
    status = models.CharField(choices=thread_status, max_length=10, default='ACTIVE')

    def __str__(self):
        return self.title


class Comment(models.Model):
    thread = models.ForeignKey(DiscussionThread, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(max_length=10000)
    created_at = models.DateTimeField(default=now)
 
    
class Bug_Report(models.Model):
    bug_status = (
        ("OPEN", "open"),
        ("RESOLVED", "resolved")
    )
    priority =(
        ("NORMAL", "normal"),
        ("LOW", "low"),
        ("HIGH", "high")
    )

    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    reporter =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reports")
    subject = models.CharField(max_length=256)
    body = models.CharField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True)
    priority = models.CharField(max_length=256, choices=priority, default="NORMAL")
    status = models.CharField(max_length=256, choices=bug_status, default="OPEN")
    file = models.FileField(upload_to='documents/%Y/%m/%d', default=None)


    def __str__(self):
        return self.subject


class Calender(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=512)
    tags = TaggableManager(blank=True)
    description = models.CharField(max_length=4096, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

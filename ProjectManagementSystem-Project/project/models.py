from django.db import models
from taggit.managers import TaggableManager
from django.conf import settings


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
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=256, choices=role_type)

    class Meta:
        unique_together =[['member_id', 'project_id']]

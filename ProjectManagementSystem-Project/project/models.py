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
    team_members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

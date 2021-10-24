from .models import *
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer


class CreateProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Project
        fields = ['id', 'project_manager', 'name', 'description', 'tags', 'started_at', 'team_members']

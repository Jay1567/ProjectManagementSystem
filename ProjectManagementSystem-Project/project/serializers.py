from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer
from accounts.models import *
from .utils import *
from django.utils import timezone


class CreateProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    team_members = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='email'
    )
    class Meta:
        model = Project
        fields = ['id', 'project_manager', 'name', 'description', 'tags', 'started_at', 'team_members']


class memberRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return str(obj)

    def to_internal_value(self, data):        
        try:
            return CustomUser.objects.get(email=data)
        except:
            validated_data={}
            validated_data['email'] = data
            validated_data['last_login'] = timezone.now()
            validated_data['is_manager'] = False
            validated_data['is_member'] = True
            user=CustomUser(**validated_data)
            user.set_unusable_password()
            user.save()
            return user

class AddMemberSerializer(serializers.ModelSerializer):
    member_id =memberRelatedField(queryset=CustomUser.objects.all() )
    class Meta:
        model = Project_Assignees
        fields = ['id', 'member_id', 'project_id', 'role']

    def validate(self, attrs):
        val_data={}; 
        val_data['email'] = attrs['member_id']
        request = self.context['request'].user
        sendInvitation(request, val_data)
        return attrs


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'project_id', 'deadline', 'subject', 'details',
            'status', 'priority', 'assignees', 'assign_date']


class DiscussionThreadSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = DiscussionThread
        fields = ['id', 'project_id', 'user', 'title', 'body', 'created_at', 'status', 'tags']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'thread', 'user', 'message', 'created_at']


class DiscussionThreadNestedSerializer(TaggitSerializer, serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_set')
    tags = TagListSerializerField()

    class Meta:
        model = DiscussionThread
        fields = ['id', 'project_id', 'user', 'title', 'body', 'created_at', 'status', 'tags', 'comments']
        
class GetMembersSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField(source='member_id.email')
    member_id = serializers.ReadOnlyField(source='member_id.id')
    class Meta:
        model = Project_Assignees
        fields =['id', 'role', 'email', 'member_id']

class EditMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Assignees
        fields = ['role',]


class CreateReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug_Report
        fields = ['project_id', 'reporter', 'subject', 'body', 'created', 'updated', 'priority', 'status', 'file']


class EditReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bug_Report
        fields = ['subject', 'body','priority', 'status']


class CalenderSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Calender
        fields = ['id', 'user', 'event_name', 'tags', 'description', 'start_time', 'end_time', 'email']

from rest_framework import serializers, pagination
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_framework.authtoken.models import Token
from .models import *


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    is_manager = serializers.BooleanField(default=False)
    is_member = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password1', 'is_manager', 'is_member')

    def get_cleaned_data(self):
        data_dict = super(CustomRegisterSerializer, self).get_cleaned_data()
        data_dict['email'] = self.validated_data.get('email', None)
        data_dict['password1'] = self.validated_data.get('password1', '')
        data_dict['is_manager'] = self.validated_data.get('device_id', '')
        data_dict['is_member'] = self.validated_data.get('is_publisher', '')
        return data_dict


class CustomLoginSerializer(RestAuthLoginSerializer):
    username = None

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['email'] = self.validated_data.get('email', '')
        return data_dict


class CustomUserDetailsSerializer(serializers.ModelSerializer):
    username = None

    class Meta:
        model = CustomUser
        fields = ('email', 'full_name', 'email_authenticated', 'is_manager', 'is_member',)
        read_only_fields = ('email', 'email_authenticated')


class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']

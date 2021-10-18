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

    def save(self, request):
        user=super().save(request)
        user.is_manager = self.validated_data.get('is_manager')
        user.is_member = self.validated_data.get('is_member')
        user.save()
        return user



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
        fields = ('email', 'full_name', 'is_manager', 'is_member', 'mobile')
        # read_only_fields = ( '',)


class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key', 'user']


class CustomOTPTokenSerializer(serializers.Serializer):
    key = serializers.CharField()
    user_id=serializers.CharField()
    user = serializers.IntegerField(source="user_id")



from rest_auth.serializers import PasswordResetSerializer
class CustomUserPasswordResetSerializer( PasswordResetSerializer):
    def get_email_options(self):
        return {
                'email_template_name': 'registration/password_reset_email.html',
                'html_email_template_name': 'registration/password_reset_email.html',
        }


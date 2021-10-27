from django.contrib.auth.models import User
from rest_framework import serializers, pagination
from rest_auth.registration.serializers import RegisterSerializer
from rest_auth.serializers import LoginSerializer as RestAuthLoginSerializer
from rest_auth.serializers import PasswordResetSerializer
from rest_framework.authtoken.models import Token
from .models import *
from rest_auth.serializers import PasswordResetSerializer
from .forms import *
from allauth.account.models import EmailAddress


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    # is_manager = serializers.BooleanField(default=True)
    # is_member = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password1')

    # def save(self, request):
    #     user=super().save(request)
    #     user.is_manager = self.validated_data.get('is_manager')
    #     user.is_member = self.validated_data.get('is_member')
    #     user.save()
    #     return user


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
    user_id = serializers.CharField()
    user = serializers.IntegerField(source="user_id")




class CustomUserPasswordResetSerializer( PasswordResetSerializer):
    password_reset_form_class = PwddResetForm
    def get_email_options(self):
        return {
                # 'email_template_name': 'registration/password_reset_email.html',
                # 'html_email_template_name': 'registration/html_password_reset_email.html', #Uncomment this when actual mail sent on email client.
        }


class sendInvitationSerializer(serializers.ModelSerializer):
    username = None
    email = serializers.EmailField()
    is_member = serializers.BooleanField(default=True)
    is_manager = serializers.BooleanField(default=False)

    class Meta:
        model = CustomUser
        fields = ('email', 'is_member', 'is_manager')
        

    def create(self, validated_data):
        try:
            member=CustomUser.objects.get(email = validated_data['email'])

            if member.is_member == False:
                member.is_member = True
                member.save()
                return member

        except CustomUser.DoesNotExist:
            user=CustomUser(**validated_data)
            user.set_unusable_password()
            user.save()

            validated_data.pop('is_manager')
            validated_data.pop('is_member')
            validated_data['user_id'] = user.id
            validated_data['verified'] = True
            validated_data['primary'] = True

            member = EmailAddress.objects.create(**validated_data)
            member.save()
            return user 

from django.core.mail import send_mail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse
from django.contrib.sites.models import Site
from django.utils.encoding import smart_bytes
from allauth.account.models import EmailAddress
from accounts.models import *


def send_mail_to_new_member(member, user):

    mail_subject = "Invitation for MyTask"
    to_email = member.email
    current_site = Site.objects.get_current()
    uidb64 = urlsafe_base64_encode(smart_bytes(member.id))
    token = PasswordResetTokenGenerator().make_token(member)
    relativeLink = reverse(
        'password_reset_confirm', kwargs={'uidb64':uidb64, 'token': token}
    )
    absurl = 'http://'+current_site.domain +relativeLink  
    message = "You are invited as project collabrator on MyTask by %s . For login go to forgot password and add your email to generate new password. %s" % (user, absurl) 

    send_mail(
        subject = mail_subject,
        message=message,
        from_email=None,
        recipient_list=[to_email],
        fail_silently=False,
    )



def send_mail_to_existing_member(member, user):
    mail_subject = "Invitation for MyTask"
    message = "You are invited as project collabrator on MyTask by %s. Login with your current credentials." % user
    to_email = member.email
    send_mail(
        subject = mail_subject,
        message=message,
        from_email=None,
        recipient_list=[to_email],
        fail_silently=False,
    )


def sendInvitation(request, validated_data):
    member=CustomUser.objects.get(email = validated_data['email'])
    try:
        EmailAddress.objects.get(email = validated_data['email'])

        if member.is_member == False:
            member.is_member = True
            member.save()
        send_mail_to_existing_member(member, request.email)

    except:
        validated_data['email'] = member.email
        validated_data['user_id'] = member.id
        validated_data['verified'] = True
        validated_data['primary'] = True
        EmailAddress.objects.create(**validated_data)
        send_mail_to_new_member(member, request.email)
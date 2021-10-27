from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
from django.core.mail import send_mail


def get_user():
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    return request


@receiver(post_save, sender=CustomUser)
def send_invitation(sender, instance, created, **kwargs):
    if created:
        if instance.is_member == True:
            current_user = get_user()
            mail_subject = "Invitation for MyTask"
            message = "You are invited as project collabrator on MyTask by %s . For login go to forgot password and add your email to generate new password." % current_user.user
            to_email = instance.email
            send_mail(
                subject = mail_subject,
                message=message,
                from_email=None,
                recipient_list=[to_email],
                fail_silently=False,
            )
    else:
        if instance.is_member == True:
            current_user = get_user()
            mail_subject = "Invitation for MyTask"
            message = "You are invited as project collabrator on MyTask by %s. Login with your current credentials." % current_user.user
            to_email = instance.email
            send_mail(
                subject = mail_subject,
                message=message,
                from_email=None,
                recipient_list=[to_email],
                fail_silently=False,
            )
        
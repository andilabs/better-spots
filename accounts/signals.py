import uuid

from accounts.tasks import send_asynchronous_email
from django.conf import settings
from django.urls import reverse


def verify_email(sender, instance, created, **kwargs):
    if created and not instance.mail_verified:
        email_verification = sender(
            verification_key=uuid.uuid4().hex[:21],
            user=instance)
        email_verification.save()


def send_email(sender, instance, created, **kwargs):

    if created:
        subject = "Verify your e-mail to activate your account."
        activation_url = 'http://{domain}{uri}'.format(
            domain=settings.INSTANCE_DOMAIN,
            uri=reverse('accounts:email_verification', kwargs={'verification_key': instance.verification_key})
        )
        mail_content = "Please click this link to activate your account\n {activation_url}".format(
            activation_url=activation_url
        )
        send_asynchronous_email.apply_async(kwargs={
            'subject': subject,
            'mail_content': mail_content,
            'recipients_emails': [instance.user.email]
        })

from __future__ import absolute_import, unicode_literals
from celery.decorators import task

from django.conf import settings
from django.core.mail import EmailMessage


@task()
def send_asynchronous_email(subject, mail_content, recipients_emails):
    msg = EmailMessage(
        subject=subject,
        body=mail_content,
        from_email=settings.EMAIL_HOST_USER,
        to=recipients_emails
    )
    msg.send()



@task()
def add(x, y):
    return x + y

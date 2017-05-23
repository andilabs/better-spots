import base64
import uuid

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from accounts.managers import UserManager
from utils.models import TimeStampedModel


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    mail_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    favourites = models.ManyToManyField('core.Spot', through='accounts.UserFavouritesSpotList', related_name='users')

    objects = UserManager()

    USERNAME_FIELD = 'email'


class EmailVerification(TimeStampedModel):
    verification_key = models.CharField(max_length=21, unique=True)
    key_timestamp = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User)


class UsersSpotsList(TimeStampedModel):

    spot = models.ForeignKey('core.Spot')
    user = models.ForeignKey(User)

    class Meta:
        abstract = True
        unique_together = ("user", "spot")


class UserFavouritesSpotList(UsersSpotsList):
    pass


# TODO move signals to seperate module and new style using apps
# TODO use fuckin async celery like solution please
@receiver(post_save, sender=User)
def verify_email(sender, instance, created, *args, **kwargs):
    if created and not instance.mail_verified:
        email_verification = EmailVerification(
            verification_key=base64.urlsafe_b64encode(uuid.uuid4().bytes)[:21],
            user=instance)
        email_verification.save()


@receiver(post_save, sender=EmailVerification)
def send_email(sender, instance, created, *args, **kwargs):

    if created:
        subject = "Verify your e-mail to activate your account."
        activation_url = 'http://{domain}{uri}'.format(
            domain=settings.INSTANCE_DOMAIN,
            uri=reverse('accounts:email_verification', kwargs={'verification_key': instance.verification_key})
        )
        mail_content = "Please click this link to activate your account\n {activation_url}".format(
            activation_url=activation_url
        )
        from .tasks import send_asynchronous_email
        #TODO switch to apply_async
        send_asynchronous_email.delay(
            subject=subject,
            mail_content=mail_content,
            recipients_emails=[instance.user.email]
        )

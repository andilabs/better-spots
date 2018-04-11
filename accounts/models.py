import uuid

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from accounts.managers import UserManager
from accounts.tasks import send_asynchronous_email

from utils.models import TimeStampedModel
from utils.signer import encrypt_data


class User(AbstractBaseUser, TimeStampedModel, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name='email address')
    mail_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    favourites = models.ManyToManyField('core.Spot', through='accounts.UserFavouritesSpotList', related_name='accounts')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, api):
        """Does the user have permissions to view the app `api`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UsersSpotsList(TimeStampedModel):

    spot = models.ForeignKey('core.Spot', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ("user", "spot")


class UserFavouritesSpotList(UsersSpotsList):
    pass


@receiver(post_save, sender='accounts.User')
def verify_email(sender, instance, created, **kwargs):
    if created and not instance.mail_verified:

        verification_key = encrypt_data(instance.email)
        subject = "Verify your e-mail to activate your account."
        activation_url = 'http://{domain}{uri}'.format(
            domain=settings.INSTANCE_DOMAIN,
            uri=reverse('accounts:email_verification', kwargs={'verification_key': verification_key})
        )
        mail_content = "Please click this link to activate your account\n {activation_url}".format(
            activation_url=activation_url
        )
        send_asynchronous_email.apply(kwargs={
            'subject': subject,
            'mail_content': mail_content,
            'recipients_emails': [instance.email]
        })

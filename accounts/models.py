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

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, api):
        "Does the user have permissions to view the app `api`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def spot_pk_to_fav_asset_pk(self):
        """
            for given user
            filters favourites spots of user
            and returns their representation in form of dictionary
            {spot_pk: list_itme_pk}
        """
        return {u_s_l.spot.pk: '%s' % u_s_l.pk
                for u_s_l in UsersSpotsList.favourites.filter(user=self)}

    @property
    def to_be_visited(self):
        return UsersSpotsList.to_be_visited.filter(user=self)


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

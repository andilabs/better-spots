from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from django.db import models


from accounts.managers import UserManager
from utils.models import TimeStampedModel


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


class EmailVerification(TimeStampedModel):
    verification_key = models.CharField(max_length=21, unique=True)
    key_timestamp = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class UsersSpotsList(TimeStampedModel):

    spot = models.ForeignKey('core.Spot', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        unique_together = ("user", "spot")


class UserFavouritesSpotList(UsersSpotsList):
    pass


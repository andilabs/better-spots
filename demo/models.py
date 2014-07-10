#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


SEX = (
    (0, 'female'),
    (1, 'male'),
)


class Dog(models.Model):
    name = models.CharField(max_length=254)
    sex = models.BooleanField(choices=SEX)
    bred = models.CharField(max_length=254, default="not specified")
    comment = models.CharField(max_length=254)

    def __unicode__(self):
        return self.name


class DogspotUserManager(BaseUserManager):

    def create_user(self, email, password=None, mail_sent=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            mail_sent=mail_sent,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, mail_sent=True):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email,
                                password=password,
                                mail_sent=mail_sent,
                                )
        user.is_admin = True
        user.save(using=self._db)
        return user


class DogspotUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address',
    )
    mail_sent = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = DogspotUserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['mail_sent', ]

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    # On Python 3: def __str__(self):
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


class EmailVerification(models.Model):
    verification_key = models.CharField(max_length=36, unique=True)
    key_timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(DogspotUser)

    def __unicode__(self):
        return "%s %s %s" % (
            self.verification_key,
            self.key_timestamp,
            self.user.email
            )

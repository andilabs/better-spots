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
        user = self.create_user(
            email,
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


SPOT_TYPE = (
    (1, 'cafe'),
    (2, 'restaurant'),
    (3, 'store'),
    (4, 'institution'),
    (5, 'pet store'),  # google type: pet_store
    (6, 'park'),
    (7, 'bar'),
    (8, 'art gallery or museum'),  # google types: art_gallery + museum
    (9, 'veterinary care'),  # google type: veterinary_care
    (10, 'hotel'),
)


class Spot(models.Model):
    name = models.CharField(max_length=250)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    address_street = models.CharField(max_length=254, default='')
    address_number = models.CharField(max_length=10, default='')
    address_city = models.CharField(max_length=100, default='')
    address_country = models.CharField(max_length=100, default='')
    spot_type = models.IntegerField(max_length=3, choices=SPOT_TYPE)
    is_accepted = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, default='')

    @property
    def friendly_rate(self):

        all_raitings_of_spot = Raiting.objects.filter(spot_id=self.id)
        sum_of_ratings = sum(i.friendly_rate for i in all_raitings_of_spot)

        if all_raitings_of_spot:
            return sum_of_ratings/float(len(all_raitings_of_spot))
        else:
            return -1.0

    @property
    def dogs_allowed(self):

        all_raitings_of_spot = Raiting.objects.filter(spot_id=self.id)

        if all_raitings_of_spot:

            sum_of_allowed = sum(i.dogs_allowed for i in all_raitings_of_spot)

            if sum_of_allowed > len(all_raitings_of_spot)/2:
                return True

            else:
                return False

        else:
            return False

    @property
    def raitings(self):
        return Raiting.objects.filter(spot_id=self.id)

    def __unicode__(self):
        return self.name

LIKERT = (
    (1, 'terrible'),
    (2, 'poor'),
    (3, 'average'),
    (4, 'very good'),
    (5, 'exccelent'),
)

DOGS_ALLOWED = (
    (0, 'Not allowed'),
    (1, 'Allowed'),
)


class Raiting(models.Model):
    data_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(DogspotUser)
    spot = models.ForeignKey(Spot)
    dogs_allowed = models.BooleanField(choices=DOGS_ALLOWED)
    friendly_rate = models.PositiveIntegerField(choices=LIKERT)

    @property
    def opinion(self):
        opinion = Opinion.objects.filter(raiting=self)
        if opinion:
            return opinion
        else:
            return None

    def __unicode__(self):
        return "%s %s by: %s rate: %2.f" % (
            self.spot.name,
            DOGS_ALLOWED[self.dogs_allowed][1],
            self.user.email,
            self.friendly_rate
            )


class Opinion(models.Model):
    raiting = models.OneToOneField(Raiting, primary_key=True)
    opinion_text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.opinion_text

    @property
    def opinion_usefulnes_raitings(self):
        return OpinionUsefulnessRating.objects.filter(opinion=self)


VOTE = (
    (1, 'Upvote'),
    (-1, 'Downvote'),
)


class OpinionUsefulnessRating(models.Model):
    opinion = models.ForeignKey(Opinion)
    user = models.ForeignKey(DogspotUser)
    vote = models.IntegerField(max_length=1, choices=VOTE)


LIST_ROLES = (
    (1, 'Favorites'),
    (2, 'To be visited'),
)


class UsersSpotsList(models.Model):
    data_added = models.DateTimeField(auto_now_add=True)
    spot = models.ForeignKey(Spot)
    user = models.ForeignKey(DogspotUser)
    role = models.IntegerField(max_length=1, choices=LIST_ROLES)

    def __unicode__(self):
        return "%s where: %s by: %s " % (
            LIST_ROLES[self.role-1][1],
            self.spot.name,
            self.user.email
            )

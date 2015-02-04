#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

from image_cropping import ImageCropField, ImageRatioField
from easy_thumbnails.files import get_thumbnailer

from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.utils.text import slugify


from accounts.models import SpotUser


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


def get_image_path(instance, filename):
    return os.path.join('img', uuid.uuid4().hex)


class Spot(models.Model):
    name = models.CharField(max_length=250)
    location = models.PointField(max_length=40, null=True)
    address_street = models.CharField(max_length=254, default='')
    address_number = models.CharField(max_length=10, default='')
    address_city = models.CharField(max_length=100, default='')
    address_country = models.CharField(max_length=100, default='')
    spot_type = models.IntegerField(max_length=3, choices=SPOT_TYPE)
    is_accepted = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, default='')
    email = models.EmailField(blank=True, null=True)
    www = models.URLField(blank=True, null=True)
    facebook = models.CharField(max_length=254, blank=True, null=True)
    is_enabled = models.NullBooleanField(default=None, null=True)
    friendly_rate = models.DecimalField(default=-1.00, max_digits=3, decimal_places=2, null=True)

    venue_photo = ImageCropField(upload_to=get_image_path, blank=True, null=True)
    cropping_venue_photo = ImageRatioField(
        'venue_photo',
        settings.VENUE_PHOTO_SIZE['W']+"x"+settings.VENUE_PHOTO_SIZE['H'],
        size_warning=True)

    spot_slug = models.SlugField(max_length=1000)
    objects = models.GeoManager()

    @property
    def thumbnail_venue_photo(self):
        if not self.venue_photo:
            return None
        thumbnail_url = get_thumbnailer(self.venue_photo).get_thumbnail({
            'size': (int(settings.VENUE_PHOTO_SIZE['W']), int(settings.VENUE_PHOTO_SIZE['H'])),
            'box': self.cropping_venue_photo,
            'crop': True,
            'detail': True, }).url
        return thumbnail_url


    @property
    def facebook_url(self):
        facebook_url = "http://www.facebook.com/%s" % self.facebook if self.facebook else None
        return facebook_url

    @property
    def raitings(self):
        return Raiting.objects.filter(spot_id=self.id)

    @property
    def latitude(self):
        return self.location.coords[1]

    @property
    def longitude(self):
        return self.location.coords[0]

    @property
    def address(self):
        return "%s, %s %s" % (
            self.address_city,
            self.address_street,
            self.address_number,)

    @property
    def prepare_vcard(self):

        dane = "BEGIN:VCARD\r\n"
        dane += "VERSION:3.0\r\n"
        dane += "N:;%s\r\n" % self.name
        dane += "item1.ADR;type=HOME;type=pref:;;%s %s;%s;;;%s\r\n" % (
            self.address_street,
            self.address_number,
            self.address_city,
            self.address_country)
        dane += "EMAIL;INTERNET;PREF:%s\r\n" % self.email if self.email else ""
        dane += "TEL;WORK;VOICE;PREF:%s\r\n" % self.phone_number if self.phone_number else ""
        dane += "URL;WORK;PREF:%s\r\n" % self.www if self.www else ""
        dane += "X-SOCIALPROFILE;type=facebook:%s\r\n"  % self.facebook if self.facebook else ""
        dane += "END:VCARD\r\n"

        return dane

    @property
    def www_url(self):
        return "http://%s%s" % (settings.INSTANCE_DOMAIN, reverse(
            'www.views.spot', args=[self.pk, self.spot_slug]))

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.spot_slug = slugify(
            "%s %s %s %s %s" % (
                self.name,
                SPOT_TYPE[self.spot_type-1][1],
                self.address_city,
                self.address_street,
                self.address_number,))

        super(Spot, self).save(*args, **kwargs)


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
    user = models.ForeignKey(SpotUser)
    spot = models.ForeignKey(Spot)
    is_enabled = models.BooleanField(choices=DOGS_ALLOWED)
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
            DOGS_ALLOWED[self.is_enabled][1],
            self.user.email,
            self.friendly_rate
            )

    class Meta:
        unique_together = ("user", "spot")


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
    user = models.ForeignKey(SpotUser)
    vote = models.IntegerField(max_length=1, choices=VOTE)


LIST_ROLES = (
    (1, 'Favorites'),
    (2, 'To be visited'),
)


class UsersSpotsList(models.Model):
    data_added = models.DateTimeField(auto_now_add=True)
    spot = models.ForeignKey(Spot)
    user = models.ForeignKey(SpotUser)
    role = models.IntegerField(max_length=1, choices=LIST_ROLES)


@receiver(post_save, sender=Raiting)
def update_spot_ratings(instance, **kwags):

    spot = instance.spot

    all_raitings_of_spot = Raiting.objects.filter(spot_id=spot.id)
    spot_rate = sum(
        i.friendly_rate for i in all_raitings_of_spot) / float(
        len(all_raitings_of_spot))

    spot_allowance = True if sum(
        i.is_enabled for i in all_raitings_of_spot) > len(
        all_raitings_of_spot) / 2 else False

    spot.friendly_rate = spot_rate
    spot.is_enabled = spot_allowance
    spot.save()

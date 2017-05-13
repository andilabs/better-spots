#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropField, ImageRatioField
from solo.models import SingletonModel

from django.conf import settings
from django.contrib.gis.db import models
from django.contrib.gis.db.models.manager import GeoManager
from django.contrib.postgres.fields import HStoreField
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

from utils.models import TimeStampedModel


def get_image_path(instance, filename):
    try:
        extension = filename.split('.')[-1]
    except IndexError:
        extension = ''
    return os.path.join(
        'img',
        '%s.%s' % (uuid.uuid4().hex, extension)
    )


class Instance(SingletonModel, TimeStampedModel):
    name = models.CharField(max_length=254, default='', blank=True, null=True)
    slogan = models.CharField(max_length=254, default='', blank=True, null=True)
    subject = models.CharField(max_length=254, default='', blank=True, null=True)
    main_color = models.CharField(max_length=254, default='', blank=True, null=True)
    description = models.TextField()
    windows_phone_store_url = models.URLField(max_length=1023, blank=True, null=True)
    google_store_url = models.URLField(max_length=1023, blank=True, null=True)
    apple_store_url = models.URLField(max_length=1023, blank=True, null=True)
    instagram = models.CharField(max_length=254, blank=True, null=True)
    facebook = models.CharField(max_length=254, blank=True, null=True)
    twitter = models.CharField(max_length=254, blank=True, null=True)
    blogger_photo = models.ImageField(upload_to=get_image_path, null=True, blank=True)

SPOT_TYPE = (
    (1, 'cafe'),
    (2, 'restaurant'),
    (3, 'hotel'),
    (4, 'shop-no-food'),
    (5, 'shop-with-food'),
)


class Spot(TimeStampedModel):
    name = models.CharField(max_length=250)
    location = models.PointField(max_length=40)
    address_street = models.CharField(max_length=254, default='', blank=True, null=True)
    address_number = models.CharField(max_length=10, default='', blank=True, null=True)
    address_city = models.CharField(max_length=100, default='', blank=True, null=True)
    address_country = models.CharField(max_length=100, default='', blank=True, null=True)
    spot_type = models.IntegerField(choices=SPOT_TYPE)
    is_accepted = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, default='', blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    www = models.URLField(blank=True, null=True)
    facebook = models.CharField(max_length=254, blank=True, null=True)
    is_enabled = models.NullBooleanField(default=None, null=True)
    friendly_rate = models.DecimalField(default=-1.00, max_digits=3, decimal_places=2, null=True)
    is_certificated = models.BooleanField(default=False)
    venue_photo = ImageCropField(upload_to=get_image_path, blank=True, null=True)
    cropping_venue_photo = ImageRatioField('venue_photo', settings.VENUE_PHOTO_SIZE['W']+"x"+settings.VENUE_PHOTO_SIZE['H'], size_warning=True)
    spot_slug = models.SlugField(max_length=1000)
    facilities = HStoreField(null=True)
    anonymous_creator_cookie = models.CharField(max_length=1024, blank=True, null=True)

    creator = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL)

    objects = GeoManager()

    class Meta:
        unique_together = (
            "name",
            "address_street",
            "address_number",
            "address_city",
            "address_country",
        )

    @property
    def thumbnail_venue_photo(self):
        if not self.venue_photo:
            return None

        if self.venue_photo and self.venue_photo.name == '':
            return None

        if not os.path.isfile(
            os.path.join(
                settings.MEDIA_ROOT, self.venue_photo.name)):
            return None

        thumbnail_url = get_thumbnailer(self.venue_photo).get_thumbnail({
            'size': (
                int(settings.VENUE_PHOTO_SIZE['W']),
                int(settings.VENUE_PHOTO_SIZE['H'])),
            'box': self.cropping_venue_photo,
            'crop': True,
            'detail': True, }).url
        return thumbnail_url

    def admin_thumbnail_venue_photo(self):
        if self.thumbnail_venue_photo:
            return mark_safe('<img src="%s" />' % self.thumbnail_venue_photo)
        else:
            return '(No photo)'

    def google_maps_static_image(self, zoom=16, width=400, height=200):
        if self.location:
            return mark_safe(
                '<img src="https://maps.googleapis.com/maps/api/staticmap?'
                'center=%s,%s&zoom=%s&size=%sx%s&'
                'markers=%s,%s" /><br><h2>Location: %s, %s' % (
                    self.location.coords[1],
                    self.location.coords[0],
                    zoom,
                    width,
                    height,
                    self.location.coords[1],
                    self.location.coords[0],
                    self.location.coords[1],
                    self.location.coords[0],
                )
            )

    @property
    def facebook_url(self):
        if self.facebook:
            facebook_url = "http://www.facebook.com/%s" % self.facebook
        else:
            facebook_url = None

        return facebook_url

    @property
    def ratings(self):
        return Rating.objects.filter(spot_id=self.id)

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
        dane += "EMAIL;INTERNET;PREF:%s\r\n" % (
            self.email if self.email else "")
        dane += "TEL;WORK;VOICE;PREF:%s\r\n" % (
            self.phone_number if self.phone_number else "")
        dane += "URL;WORK;PREF:%s\r\n" % (
            self.www if self.www else "")
        dane += "X-SOCIALPROFILE;type=facebook:%s\r\n" % (
            self.facebook if self.facebook else "")
        dane += "END:VCARD\r\n"

        return dane

    def is_in_user_favourites(self, user):
        return self in user.favourites

    @property
    def www_url(self):
        return "http://%s%s" % (settings.INSTANCE_DOMAIN, reverse(
            'www:spot', args=[self.pk, self.spot_slug]))

    @property
    def get_url(self):
        if self.is_certificated:
            return reverse('www:certificated_detail', args=[self.pk, self.spot_slug])
        else:
            return reverse('www:spot', args=[self.pk, self.spot_slug])

    def __str__(self):
        return self.name

    def google_maps_admin_widget(self):
        return mark_safe("""<input type="text" style="width:100%" id="us3-address"/>
                  <div id="us3" style="width: 750px; height: 400px;"></div>""")

    def save(self, *args, **kwargs):
        self.spot_slug = slugify(
            "%s %s %s %s %s" % (
                self.name,
                SPOT_TYPE[self.spot_type-1][1],
                self.address_city,
                self.address_street,
                self.address_number,)
        )

        super(Spot, self).save(*args, **kwargs)


LIKERT = (
    (1, 'terrible'),
    (2, 'poor'),
    (3, 'average'),
    (4, 'very good'),
    (5, 'exccelent'),
)

IS_ALLOWED_CHOICES = (
    (False, 'Not allowed'),
    (True, 'Allowed'),
)


class Rating(TimeStampedModel):
    data_added = models.DateTimeField(auto_now_add=True)
    is_enabled = models.BooleanField(choices=IS_ALLOWED_CHOICES, default=False)
    friendly_rate = models.PositiveIntegerField(choices=LIKERT)
    facilities = HStoreField(null=True)

    user = models.ForeignKey('accounts.User', null=True)
    spot = models.ForeignKey(Spot, related_name='ratings')

    class Meta:
        unique_together = ("user", "spot")

    @property
    def opinion(self):
        opinion = Opinion.objects.filter(rating=self)
        if opinion:
            return opinion
        else:
            return None

    @property
    def spot_pk(self):
        return self.spot.pk

    def __unicode__(self):
        return "%s %s by: %s rate: %2.f" % (
            self.spot.name,
            IS_ALLOWED_CHOICES[self.is_enabled][1],
            self.user.email,
            self.friendly_rate
        )


class Opinion(TimeStampedModel):
    opinion_text = models.CharField(max_length=500)

    rating = models.OneToOneField(Rating, primary_key=True)

    def __unicode__(self):
        return self.opinion_text

    @property
    def opinion_usefulness_ratings(self):
        return OpinionUsefulnessRating.objects.filter(opinion=self)


VOTE = (
    (1, 'Upvote'),
    (-1, 'Downvote'),
)


class OpinionUsefulnessRating(TimeStampedModel):
    vote = models.IntegerField(choices=VOTE)

    opinion = models.ForeignKey(Opinion)
    user = models.ForeignKey('accounts.User', null=True)




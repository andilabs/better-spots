#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import uuid

from unidecode import unidecode
from django_hstore import hstore
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropField, ImageRatioField
from solo.models import SingletonModel

from django.db.models.signals import post_save, post_delete
from django.conf import settings
from django.contrib.gis.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe

# from utils.img_path import get_image_path


def get_image_path(instance, filename):
    try:
        extension = filename.split('.')[-1]
    except IndexError:
        extension = ''
    return os.path.join(
        'img',
        '%s.%s' % (uuid.uuid4().hex, extension)
    )


class Instance(SingletonModel):
    name = models.CharField(
        max_length=254, default='', blank=True, null=True)
    slogan = models.CharField(
        max_length=254, default='', blank=True, null=True)
    description = models.CharField(
        max_length=254, default='', blank=True, null=True)
    subject = models.CharField(
        max_length=254, default='', blank=True, null=True)
    main_color = models.CharField(
        max_length=254, default='', blank=True, null=True)
    description = models.TextField()

    windows_phone_store_url = models.URLField(
        max_length=1023, blank=True, null=True)
    google_store_url = models.URLField(
        max_length=1023, blank=True, null=True)
    apple_store_url = models.URLField(
        max_length=1023, blank=True, null=True)

    instagram = models.CharField(
        max_length=254, blank=True, null=True)
    facebook = models.CharField(
        max_length=254, blank=True, null=True)
    twitter = models.CharField(
        max_length=254, blank=True, null=True)

    bloger_photo = models.ImageField(
        upload_to=get_image_path, null=True, blank=True)

SPOT_TYPE = (
    (1, 'cafe'),
    (2, 'restaurant'),
    (3, 'hotel'),
    (4, 'shop-no-food'),
    (5, 'shop-with-food'),
)


class Spot(models.Model):
    date_created = models.DateTimeField(
        auto_now_add=True, null=True)
    date_updated = models.DateTimeField(
        auto_now=True, null=True)
    name = models.CharField(
        max_length=250)
    location = models.PointField(
        max_length=40)
    address_street = models.CharField(
        max_length=254, default='', blank=True, null=True)
    address_number = models.CharField(
        max_length=10, default='', blank=True, null=True)
    address_city = models.CharField(
        max_length=100, default='', blank=True, null=True)
    address_country = models.CharField(
        max_length=100, default='', blank=True, null=True)
    spot_type = models.IntegerField(
        max_length=3, choices=SPOT_TYPE)
    is_accepted = models.BooleanField(
        default=False)
    phone_number = models.CharField(
        max_length=100, default='', blank=True, null=True)
    email = models.EmailField(
        blank=True, null=True)
    www = models.URLField(
        blank=True, null=True)
    facebook = models.CharField(
        max_length=254, blank=True, null=True)
    is_enabled = models.NullBooleanField(
        default=None, null=True)
    friendly_rate = models.DecimalField(
        default=-1.00, max_digits=3, decimal_places=2, null=True)
    is_certificated = models.BooleanField(
        default=False)
    venue_photo = ImageCropField(
        upload_to=get_image_path, blank=True, null=True)
    cropping_venue_photo = ImageRatioField(
        'venue_photo',
        settings.VENUE_PHOTO_SIZE['W']+"x"+settings.VENUE_PHOTO_SIZE['H'],
        size_warning=True)
    spot_slug = models.SlugField(
        max_length=1000)
    facilities = hstore.DictionaryField(
        schema=settings.HSTORE_SCHEMA)
    creator = models.ForeignKey(
        'accounts.SpotUser',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    anonymous_creator_cookie = models.CharField(
        max_length=1024, blank=True, null=True)

    objects = hstore.HStoreGeoManager()

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
        if UsersSpotsList.favourites.filter(spot=self, user=user).count():
            return True
        else:
            return False

    @property
    def www_url(self):
        return "http://%s%s" % (settings.INSTANCE_DOMAIN, reverse(
            'www.views.spot', args=[self.pk, self.spot_slug]))

    def __unicode__(self):
        return self.name

    def google_maps_admin_widget(self):
        return mark_safe("""<input type="text" style="width:100%" id="us3-address"/>
                  <div id="us3" style="width: 750px; height: 400px;"></div>""")

    def save(self, *args, **kwargs):
        self.spot_slug = slugify(unidecode(
            "%s %s %s %s %s" % (
                self.name,
                SPOT_TYPE[self.spot_type-1][1],
                self.address_city,
                self.address_street,
                self.address_number,)))

        super(Spot, self).save(*args, **kwargs)


LIKERT = (
    (1, 'terrible'),
    (2, 'poor'),
    (3, 'average'),
    (4, 'very good'),
    (5, 'exccelent'),
)

DOGS_ALLOWED = (
    (False, 'Not allowed'),
    (True, 'Allowed'),
)


class Rating(models.Model):
    data_added = models.DateTimeField(
        auto_now_add=True)
    user = models.ForeignKey(
        'accounts.SpotUser')
    spot = models.ForeignKey(
        Spot, related_name='ratings')
    is_enabled = models.BooleanField(
        choices=DOGS_ALLOWED, default=False)
    friendly_rate = models.PositiveIntegerField(
        choices=LIKERT)
    facilities = hstore.DictionaryField(
        schema=settings.HSTORE_SCHEMA)

    objects = hstore.HStoreGeoManager()

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
            DOGS_ALLOWED[self.is_enabled][1],
            self.user.email,
            self.friendly_rate
        )

    class Meta:
        unique_together = ("user", "spot")


class Opinion(models.Model):
    rating = models.OneToOneField(
        Rating, primary_key=True)
    opinion_text = models.CharField(
        max_length=500)

    def __unicode__(self):
        return self.opinion_text

    @property
    def opinion_usefulnes_ratings(self):
        return OpinionUsefulnessRating.objects.filter(opinion=self)


VOTE = (
    (1, 'Upvote'),
    (-1, 'Downvote'),
)


class OpinionUsefulnessRating(models.Model):
    opinion = models.ForeignKey(
        Opinion)
    user = models.ForeignKey(
        'accounts.SpotUser')
    vote = models.IntegerField(
        max_length=1, choices=VOTE)


class UsersFavouritesSpotsListManager(models.Manager):
    def get_queryset(self):
        return super(
            UsersFavouritesSpotsListManager, self).get_queryset().filter(
            role=1)


class UserToBeVisitedSpotsListManager(models.Manager):
    def get_queryset(self):
        return super(
            UserToBeVisitedSpotsListManager, self).get_queryset().filter(
            role=2)


LIST_KIND = (
    (1, 'Favorites'),
    (2, 'To be visited'),
)


class UsersSpotsList(models.Model):
    data_added = models.DateTimeField(
        auto_now_add=True)
    spot = models.ForeignKey(
        Spot)
    user = models.ForeignKey(
        'accounts.SpotUser')
    role = models.IntegerField(
        max_length=1, choices=LIST_KIND)

    objects = models.Manager()
    favourites = UsersFavouritesSpotsListManager()
    to_be_visited = UserToBeVisitedSpotsListManager()

    def __unicode__(self):
        return "%s: %s %s %s" % (
            dict(LIST_KIND)[self.role].upper(),
            self.user.email,
            self.spot.name,
            self.role
        )

    class Meta:
        unique_together = ("user", "spot", "role")

    @property
    def spot_pk(self):
        return self.spot.pk


@receiver(post_delete, sender=Rating)
@receiver(post_save, sender=Rating)
def update_spot_evaluations(instance, **kwags):
    spot = instance.spot
    all_ratings_of_spot = Rating.objects.filter(spot=spot)

    if all_ratings_of_spot:

        # determine average sppot RATE
        spot_rate = sum(
            i.friendly_rate for i in all_ratings_of_spot) / float(
            len(all_ratings_of_spot))
        spot.friendly_rate = spot_rate

        # determine either spot is ENABLED
        spot_enabled = True if sum(
            i.is_enabled for i in all_ratings_of_spot) > len(
            all_ratings_of_spot) / 2 else False
        spot.is_enabled = spot_enabled

    else:
        spot.friendly_rate = -1.0
        spot.is_enabled = False

    # determine each FACILITY fullfilment
    stats = {}

    for facility in [facility['name'] for facility in settings.HSTORE_SCHEMA]:
        facilities_record = [rating.facilities.get(facility)
                             for rating
                             in all_ratings_of_spot]
        stats[facility] = {
            'positive': facilities_record.count(True),
            'all': len(facilities_record)-facilities_record.count(None)
        }

    for facility, counts in stats.items():

        if counts['all'] > 0:
            positive_ratio = counts['positive'] / float(counts['all'])
            if not spot.facilities:
                spot.facilities = {}

            if positive_ratio > 0.5:
                spot.facilities[facility] = True
            else:
                spot.facilities[facility] = False

    spot.save()

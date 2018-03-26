import os

from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropField, ImageRatioField

from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.geocoding import reverse_geocoding
from utils.img_path import get_image_path
from utils.models import TimeStampedModel, Tag


SPOT_TYPE_CHOICES = (
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

    spot_type = models.IntegerField(choices=SPOT_TYPE_CHOICES)

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

    anonymous_creator_cookie = models.CharField(max_length=1024, blank=True, null=True) #TODO needed?

    creator = models.ForeignKey('accounts.User', null=True, blank=True, on_delete=models.SET_NULL) #TODO rethink it

    tags = models.ManyToManyField(Tag, related_name='spot_facilities', null=True, blank=True)

    @property
    def thumbnail_venue_photo(self):
        if not self.venue_photo:
            return None

        if self.venue_photo and self.venue_photo.name == '':
            return None

        if not os.path.isfile(os.path.join(settings.MEDIA_ROOT, self.venue_photo.name)):
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
            return mark_safe('<img src="{}" width="175" height="75"/>'.format(self.thumbnail_venue_photo))
        else:
            return '(No photo)'

    def google_maps_static_image(self, zoom=16, width=400, height=200):
        if self.location:
            return mark_safe(
                '<img src="https://maps.googleapis.com/maps/api/staticmap?'
                'center={latitude},{longitude}&zoom={zoom}&size={width}x{height}&'
                'markers={latitude},{longitude}" /><br><h2>Location: {latitude},{longitude}'.format(
                    latitude=self.location.coords[1],
                    longitude=self.location.coords[0],
                    zoom=zoom,
                    width=width,
                    height=height
                )
            )

    @property
    def facebook_url(self):
        if self.facebook:
            facebook_url = "http://www.facebook.com/{}".format(self.facebook)
        else:
            facebook_url = None

        return facebook_url

    @property
    def ratings(self):
        from core.models.ratings import Rating
        return Rating.objects.filter(spot_id=self.id)

    @property
    def latitude(self):
        return self.location.coords[1]

    @property
    def longitude(self):
        return self.location.coords[0]

    @property
    def address(self):
        return "{}, {} {}".format(
            self.address_city,
            self.address_street,
            self.address_number
        )

    @property
    def prepare_vcard(self):
        vcard = "BEGIN:VCARD\r\n"
        vcard += "VERSION:3.0\r\n"
        vcard += "N:;{}\r\n".format(self.name)
        vcard += "item1.ADR;type=HOME;type=pref:;;{} {};{};;;{}\r\n".format(
            self.address_street,
            self.address_number,
            self.address_city,
            self.address_country)
        if self.email:
            vcard += "EMAIL;INTERNET;PREF:{}\r\n".format(self.email)
        if self.phone_number:
            vcard += "TEL;WORK;VOICE;PREF:{}\r\n".format(self.phone_number)
        if self.www:
            vcard += "URL;WORK;PREF:{}\r\n".format(self.www)
        if self.facebook:
            vcard += "X-SOCIALPROFILE;type=facebook:{}\r\n".format(self.facebook)
        vcard += "END:VCARD\r\n"
        return vcard

    def is_in_user_favourites(self, user):
        return self in user.favourites

    @property
    def www_url(self):
        return reverse('www:spot', args=[self.pk, self.spot_slug])

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

    @staticmethod
    def slugify(name, spot_type, city, street, address_number):
        return slugify(
            "{} {} {} {} {}".format(
                name,
                spot_type,
                city,
                street,
                address_number
            )
        )


@receiver(post_save, sender='core.Spot')
def fill_address_based_on_reverse_geocoding(sender, instance, created, **kwargs):
    longitude, latitude = instance.location.coords
    address_info = reverse_geocoding(latitude=latitude, longitude=longitude)
    sender.objects.filter(
        pk=instance.pk
    ).update(
        address_number=address_info.get('address_number'),
        address_street=address_info.get('address_street'),
        address_city=address_info.get('address_city'),
        address_country=address_info.get('address_country'),
        spot_slug=Spot.slugify(
            name=instance.name,
            spot_type=instance.get_spot_type_display(),
            city=address_info.get('address_city'),
            street=address_info.get('address_street'),
            address_number=address_info.get('address_number')
        )
    )

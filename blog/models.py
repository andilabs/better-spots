#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from unidecode import unidecode
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropField, ImageRatioField

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.template.defaultfilters import slugify

from core.models import Spot
from utils.img_path import get_image_path


class DraftsManager(models.Manager):
    def get_queryset(self):
        return super(DraftsManager, self).get_queryset().filter(
            published_date__isnull=True)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            published_date__isnull=False)


class Post(models.Model):
    user = models.ForeignKey(
        'accounts.SpotUser',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    title = models.CharField(
        max_length=200)
    text = models.TextField(
        help_text='blog note text')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True,
        null=True,
        help_text='Saving with empty values makes post unpublished')
    spot = models.ForeignKey(
        Spot,
        null=True,
        blank=True,
        related_name='blog_posts')
    blogpost_photo = ImageCropField(
        upload_to=get_image_path,
        blank=True,
        null=True)
    cropping_blogpost_photo = ImageRatioField(
        'blogpost_photo',
        '%sx%s' % (
            settings.BLOGPOST_PHOTO_SIZE['W'],
            settings.BLOGPOST_PHOTO_SIZE['H']),
        size_warning=True)
    post_slug = models.SlugField(
        max_length=1200)
    objects = models.Manager()
    drafts = DraftsManager()
    published = PublishedManager()

    @property
    def blogpost_photo_thumb(self):
        """
            serves url of image with default resolution set in settings
        """
        return self._blogpost_photo_thumb()

    def admin_blogpost_photo_thumb(self):
        if self.blogpost_photo:
            return '<img src="%s" />' % self._blogpost_photo_thumb(
                width=500, height=500)
        else:
            return '(No photo)'

    admin_blogpost_photo_thumb.short_description = 'Admin blogpost photo thumb'
    admin_blogpost_photo_thumb.allow_tags = True

    def _blogpost_photo_thumb(self,
                              width=int(settings.BLOGPOST_PHOTO_SIZE['W']),
                              height=int(settings.BLOGPOST_PHOTO_SIZE['H'])):

        if not self.blogpost_photo:
            return None

        if self.blogpost_photo and self.blogpost_photo.name == '':
            return None

        if not os.path.isfile(
            os.path.join(
                settings.MEDIA_ROOT, self.blogpost_photo.name)):
            return None

        thumbnail_url = get_thumbnailer(self.blogpost_photo).get_thumbnail({
            'size': (width, height),
            'box': self.cropping_blogpost_photo,
            'crop': True,
            'detail': True, }).url

        return thumbnail_url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.post_slug = "%i/%i/%i/%s" % (
            self.created_date.year,
            self.created_date.month,
            self.created_date.day,
            slugify(unidecode(self.title))
        )
        super(Post, self).save(*args, **kwargs)

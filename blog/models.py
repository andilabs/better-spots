#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from easy_thumbnails.files import get_thumbnailer
from image_cropping import ImageCropField, ImageRatioField

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify


from blog.managers import DraftsManager, PublishedManager
from utils.img_path import get_image_path


class BlogPost(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    text = models.TextField(help_text='blog note text')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True, help_text='Saving with empty values makes post unpublished')
    spot = models.ForeignKey('core.Spot', null=True, blank=True, on_delete=models.CASCADE, related_name='blog_posts')
    photo = ImageCropField(upload_to=get_image_path, blank=True, null=True)
    cropping_photo = ImageRatioField('photo', '%sx%s' % (settings.BLOGPOST_PHOTO_SIZE['W'], settings.BLOGPOST_PHOTO_SIZE['H']), size_warning=True)
    post_slug = models.SlugField(max_length=1200)

    objects = models.Manager()
    drafts = DraftsManager()
    published = PublishedManager()

    @property
    def photo_thumb(self):
        """
            serves url of image with default resolution set in settings
        """
        return self._photo_thumb()

    def admin_photo_thumb(self):
        if self.photo:
            return '<img src="%s" />' % self._photo_thumb(
                width=500, height=500)
        else:
            return '(No photo)'

    admin_photo_thumb.short_description = 'Admin blogpost photo thumb'
    admin_photo_thumb.allow_tags = True

    def _photo_thumb(self, width=int(settings.BLOGPOST_PHOTO_SIZE['W']),
                     height=int(settings.BLOGPOST_PHOTO_SIZE['H'])):

        if not self.photo:
            return None

        if self.photo and self.photo.name == '':
            return None

        if not os.path.isfile(
            os.path.join(
                settings.MEDIA_ROOT, self.photo.name)):
            return None

        thumbnail_url = get_thumbnailer(self.photo).get_thumbnail({
            'size': (width, height),
            'box': self.cropping_photo,
            'crop': True,
            'detail': True, }).url

        return thumbnail_url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def get_slugged_url(self):
        return reverse('blog:blogpost_detail', args=[self.post_slug, self.pk])

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.post_slug = "{}/{}/{}/{}".format(
            self.created_date.year,
            self.created_date.month,
            self.created_date.day,
            slugify(self.title)
        )
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

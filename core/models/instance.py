#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from solo.models import SingletonModel

from utils.img_path import get_image_path
from utils.models import TimeStampedModel


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




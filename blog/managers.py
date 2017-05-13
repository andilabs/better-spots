#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class DraftsManager(models.Manager):
    def get_queryset(self):
        return super(DraftsManager, self).get_queryset().filter(
            published_date__isnull=True)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            published_date__isnull=False)
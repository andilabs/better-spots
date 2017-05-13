# -*- coding: utf-8 -*-

from django.db import models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

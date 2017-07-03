# -*- coding: utf-8 -*-

from django.db import models


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True


class Tag(models.Model):

    text = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{} (pk={})".format(self.text, self.pk)

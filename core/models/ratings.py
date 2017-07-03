#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

from core.models.spots import Spot
from utils.models import TimeStampedModel, Tag

FRIENDLY_RATE_CHOICES = (
    (1, 'terrible'),
    (2, 'poor'),
    (3, 'average'),
    (4, 'very good'),
    (5, 'excellent'),
)

IS_ALLOWED_CHOICES = (
    (False, 'Not allowed'),
    (True, 'Allowed'),
)


class Rating(TimeStampedModel):
    is_enabled = models.BooleanField(choices=IS_ALLOWED_CHOICES, default=False)
    friendly_rate = models.PositiveIntegerField(choices=FRIENDLY_RATE_CHOICES)

    user = models.ForeignKey('accounts.User', null=True) #TODO wtf it can be null?
    spot = models.ForeignKey(Spot, related_name='ratings')
    tags = models.ManyToManyField(Tag, related_name='rating_facilities', null=True, blank=True)

    class Meta:
        unique_together = ("user", "spot")

    def __str__(self):
        return "{} {} by: {} rate: {}".format(
            self.spot.name,
            dict(IS_ALLOWED_CHOICES)[self.is_enabled],
            self.user.email,
            self.friendly_rate
        )

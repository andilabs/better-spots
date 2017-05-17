#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models
from django.contrib.postgres.fields import HStoreField

from core.models.opinions import Opinion
from core.models.spots import Spot
from utils.models import TimeStampedModel


LIKERT = (
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
        return "{} {} by: {} rate: {}".format(
            self.spot.name,
            dict(IS_ALLOWED_CHOICES)[self.is_enabled],
            self.user.email,
            self.friendly_rate
        )


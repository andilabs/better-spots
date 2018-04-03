#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django.db.models import Avg
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

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

    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    spot = models.ForeignKey(Spot, related_name='ratings', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='rating_facilities', blank=True)

    class Meta:
        unique_together = ("user", "spot")

    def __str__(self):
        return "{} {} by: {} rate: {}".format(
            self.spot.name,
            self.get_is_enabled_display(),
            self.user.email,
            self.friendly_rate
        )


@receiver(post_save, sender='core.Rating')
def update_friendly_rate_and_enabled_status_of_spot(sender, instance, created, **kwargs):
    spot_ratings = Rating.objects.filter(spot_id=instance.spot.pk)
    averages = spot_ratings.aggregate(
        friendly_rate=Avg('friendly_rate'),
        is_enabled=Avg(Cast('is_enabled', IntegerField()))
    )
    averages.update({
        'is_enabled': True if averages['is_enabled'] >= 0.5 else False,
    })
    Spot.objects.filter(pk=instance.spot.pk).update(
        **averages
    )


@receiver(m2m_changed, sender=Rating.tags.through)
def update_tags_on_spot_after_rating(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action in ['post_add', 'post_remove', 'post_clear']:
        instance.spot.tags.clear()
        spot_ratings_tags_ids = Rating.objects.filter(
            spot=instance.spot,
            tags__isnull=False
        ).values_list('tags', flat=True)
        instance.spot.tags.add(*list(Tag.objects.filter(pk__in=spot_ratings_tags_ids)))


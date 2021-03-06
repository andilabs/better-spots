#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.gis.db import models

from utils.models import TimeStampedModel


class Opinion(TimeStampedModel):
    opinion_text = models.CharField(max_length=500)

    rating = models.OneToOneField('core.Rating', primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.opinion_text

    @property
    def opinion_usefulness_ratings(self):
        return OpinionUsefulnessRating.objects.filter(opinion=self)


VOTE_CHOICES = (
    (1, 'Upvote'),
    (-1, 'Downvote'),
)


class OpinionUsefulnessRating(TimeStampedModel):
    vote = models.IntegerField(choices=VOTE_CHOICES)

    opinion = models.ForeignKey('core.Opinion', on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', null=True, on_delete=models.CASCADE)

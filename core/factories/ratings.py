import factory
from factory import django
from factory.fuzzy import FuzzyChoice

from core.models.ratings import Rating


class RatingFactory(django.DjangoModelFactory):

    friendly_rate = FuzzyChoice(choice[0] for choice in Rating._meta.get_field('friendly_rate').choices)
    user =  factory.SubFactory('accounts.factories.UserFactory')

    class Meta:
        model = 'core.Rating'
        django_get_or_create = ('user', 'spot')

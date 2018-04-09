import factory

from accounts.models import User, UserFavouritesSpotList


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User
        django_get_or_create = ('email', )


class UserFavouritesSpotListFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = UserFavouritesSpotList
        django_get_or_create = ('user', 'spot')

import factory

from core.models.ratings import Rating


class InstanceFactory(factory.Factory):

    class Meta:
        model = Rating

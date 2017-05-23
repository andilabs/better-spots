import factory

from core.models.spots import Spot


class InstanceFactory(factory.Factory):

    class Meta:
        model = Spot

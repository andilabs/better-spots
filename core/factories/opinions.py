import factory

from core.models.opinions import Opinion


class InstanceFactory(factory.Factory):

    class Meta:
        model = Opinion

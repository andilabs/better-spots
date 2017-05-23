import factory

from core.models.instance import Instance


class InstanceFactory(factory.Factory):

    class Meta:
        model = Instance

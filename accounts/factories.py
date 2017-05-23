import factory

from accounts.models import User


class UserFactory(factory.Factory):

    class Meta:
        model = User


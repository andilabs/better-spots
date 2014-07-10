import datetime
from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from django.conf import settings


class ExpiringTokenAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted')

        time_now = datetime.datetime.now()

        if token.created < time_now - datetime.timedelta(
                hours=settings.TOKEN_EXPIRES_AFTER):
            raise exceptions.AuthenticationFailed('Token has expired')

        return (token.user, token)

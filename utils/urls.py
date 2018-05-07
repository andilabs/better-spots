import functools
from django.conf import settings


def with_absolute_url(method):
    @functools.wraps(method)
    def wrapper(self, obj=None):
        try:
            request = self.context['request']
            host = request.get_host()
            is_secure = request.is_secure()
        except (AttributeError, KeyError):
            host = settings.INSTANCE_DOMAIN
            is_secure = False
        return "{http_or_https}://{host_with_port}{relative_url}".format(
            http_or_https='https' if is_secure else 'http',
            host_with_port=host,
            relative_url=method(self, obj) if obj else method(self)
        )
    return wrapper

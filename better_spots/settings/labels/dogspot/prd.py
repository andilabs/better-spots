from .base import *


RAVEN_CONFIG = {
    'dsn': 'https://{raven_config_sentry_key}:c9cd00443c434d5fb1b204d8e5a95ffa@app.getsentry.com/29551'.format(
        raven_config_sentry_key=os.environ['RAVEN_CONFIG_SENTRY_KEY']
    ),
}

INSTANCE_DOMAIN = "dogspot.eu"

EMAIL_HOST_USER = 'no-reply@dogspot.eu'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

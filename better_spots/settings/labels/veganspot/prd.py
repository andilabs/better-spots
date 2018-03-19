from .base import *


RAVEN_CONFIG = {
    'dsn': 'https://{raven_config_sentry_key}:2b007aed601c4cacaa72ce45443f3db7@app.getsentry.com/37314'.format(
        raven_config_sentry_key=os.environ['RAVEN_CONFIG_SENTRY_KEY']
    ),
}

INSTANCE_DOMAIN = "veganspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@veganspot.eu'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD_PROD']

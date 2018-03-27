from .base import *


RAVEN_CONFIG = {
    'dsn': 'https://{raven_config_sentry_key}:67601b0d9cc34321b6a38b31e1b79e22@app.getsentry.com/37317'.format(
        raven_config_sentry_key=os.environ['RAVEN_CONFIG_SENTRY_KEY']
    ),
}

INSTANCE_DOMAIN = "enabledspot.eu"

EMAIL_USE_TLS = True
EMAIL_HOST = 'poczta.superhost.pl'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'no-reply@enabledspot.eu'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

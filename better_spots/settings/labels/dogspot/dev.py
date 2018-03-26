from .base import *

DEBUG = True

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'localhost.debug@gmail.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

INSTANCE_DOMAIN = '127.0.0.1:9000'

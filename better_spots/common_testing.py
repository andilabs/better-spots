import os

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = os.environ['MAILTRAP_USER']
EMAIL_HOST_PASSWORD = os.environ['MAILTRAP_PASSWORD']
EMAIL_PORT = '2525'

INSTANCE_DOMAIN = 'testserver'

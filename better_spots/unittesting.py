import os
from better_spots.settings import *


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


MIGRATION_MODULES = DisableMigrations()

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = os.environ['MAILTRAP_USER']
EMAIL_HOST_PASSWORD = os.environ['MAILTRAP_PASSWORD']
EMAIL_PORT = '2525'

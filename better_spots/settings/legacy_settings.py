# TODO clean it this is legacy
# from unipath import Path
#
# PROJECT_ROOT_PATH = Path(__file__).ancestor(3)
#
# STATICFILES_DIRS = (
#     PROJECT_ROOT_PATH.child('static_assets'),
# )
#
# MEDIA_URL = '/media/'
#
# STATIC_URL = '/static/'
#
#
# if 'dogspot.eu' in PROJECT_ROOT_PATH.split('/'):
#     SPOT_PROJECT_NAME = 'dogspot'
#
#
# elif 'momspot.eu' in PROJECT_ROOT_PATH.split('/'):
#     from better_spots.settings.labels.momspot import *
#     SPOT_PROJECT_NAME = 'momspot'
#
#
# elif 'enabledspot.eu' in PROJECT_ROOT_PATH.split('/'):
#     SPOT_PROJECT_NAME = 'enabledspot'
#
#
# elif 'veganspot.eu' in PROJECT_ROOT_PATH.split('/'):
#     SPOT_PROJECT_NAME = 'veganspot'
#
# else:
#     from .local import *
#
# SPOT_PROJECT_FAVICON_URL = os.path.join(
#     'static',
#     SPOT_PROJECT_NAME,
#     'favicon.ico'
# )
#
# SPOT_PROJECT_BLOGGER_PHOTO = os.path.join(STATIC_URL, SPOT_PROJECT_NAME, 'blogger_photo.jpg')

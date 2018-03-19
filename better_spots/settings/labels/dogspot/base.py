from better_spots.settings.common import *

INSTANCE_DOMAIN = "dogspot.eu"

EMAIL_HOST_USER = 'no-reply@dogspot.eu'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25


SPOT_PROJECT_NAME = 'dogspot'

SPOT_PROJECT_SLOGAN = 'Wow the World!'

SPOT_PROJECT_DESCRIPTION = 'find dog friendly cafes, restaurants and more'

SPOT_PROJECT_SUBJECT = 'Dog'

SPOT_PROJECT_MAIN_COLOR = '#fcbd41'

SPOT_PROJECT_INSTAGRAM_URL = "https://www.instagram.com/dogspoteu/"

TAGS = {
    1: 'fresh water',
    2: 'dedicated menu',
    3: 'snacks',
}

SPOT_PROJECT_FAVICON_URL = os.path.join(
    'static',
    SPOT_PROJECT_NAME,
    'favicon.ico'
)

SPOT_PROJECT_BLOGGER_PHOTO = os.path.join(STATIC_URL, SPOT_PROJECT_NAME, 'blogger_photo.jpg')

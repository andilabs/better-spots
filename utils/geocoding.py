import requests

from django.conf import settings
from django.utils.http import urlquote

GEOCODING_URL = "http://maps.googleapis.com/maps/api/geocode/json?address={address}&sensor=false"


def geocoding(address):
    """ makes request to Google Maps API, and returns
        latitude and longitude for given address

    :param address: string in form like: 'Warszawa Kolejowa 47'
    :return: dict with latitude and longitude like: {u'lat': 52.2263065, u'lng': 20.9828942}
    """
    url = GEOCODING_URL.format(
        address=urlquote(address.replace(' ', '+'))
    )
    response = requests.get(url)
    info = response.json().get("results")[0].get("geometry").get("location")
    return info


REVERSE_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"


def reverse_geocoding(latitude, longitude):

    url = REVERSE_GEOCODING_URL.format(
        latitude=latitude,
        longitude=longitude,
        api_key=settings.GOOGLE_MAP_API_KEY
    )
    response = requests.get(url)
    info = response.json()
    address = {}

    for component in info['results'][0]['address_components']:
        if 'street_number' in component.get('types'):
            address['address_number'] = component['long_name']
        if 'route' in component.get('types'):
            address['address_street'] = component['long_name']
        if 'locality' in component.get('types'):
            address['address_city'] = component['long_name']
        if 'country' in component.get('types'):
            address['address_country'] = component['long_name']

    return address

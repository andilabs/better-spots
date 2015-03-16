import urllib
import json

from django.utils.http import urlquote

def geocode(address):
    """
        This method for given in parameter:
        arguments:
        address -- string in form like: 'Warszawa Kolejowa 47'

        makes request to Google Maps API, and returns
        dict with latitude and longitude like: {u'lat': 52.2263065, u'lng': 20.9828942}

    """
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" \
          % (urlquote(address.replace(' ', '+')))
    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")
    return info

geocode('Warszawa Kolejowa 47')
import urllib
import json

from django.utils.http import urlquote

YOUR_API_KEY = "AIzaSyBj2VxTkcBPQ9yOXerWQUil-pzMuTaz4Ao"


def geocode(addr):
    """
        This method for given in parameter address makes request to Google Maps API, and returns latitude and longitude
    """

    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" \
          % (urlquote(addr.replace(' ', '+')))

    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")

    return info
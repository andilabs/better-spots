foursquare API
==============


venues API endpoint
-------------------


.. http:get:: https://api.foursquare.com/v2/venues/search?ll={lat},{lng}&client_id={CLEINT_ID}&client_secret={CLIENT_SECRET}&v=20150316

credentials to app can be found here:

    https://de.foursquare.com/developers/app/VYFRCYBKV24XBIUAJJEFQW4ENIKSGRPBYBTOTQK5H0YNX4YO

Example response:

.. sourcecode:: json

    {
      "meta": {
        "code": 200
      },
      "response": {
        "venues": [
          {
            "id": "53db71e1498e2c14888150ef",
            "name": "Bułkę przez Bibułkę",
            "contact": {},
            "location": {
              "address": "Zgody 3",
              "lat": 52.23260684753594,
              "lng": 21.0137436220574,
              "distance": 16,
              "cc": "PL",
              "country": "Poland",
              "formattedAddress": [
                "Zgody 3",
                "Poland"
              ]
            },
            "categories": [
              {
                "id": "4bf58dd8d48988d16d941735",
                "name": "Café",
                "pluralName": "Cafés",
                "shortName": "Café",
                "icon": {
                  "prefix": "https://ss3.4sqi.net/img/categories_v2/food/cafe_",
                  "suffix": ".png"
                },
                "primary": true
              }
            ],
            "verified": false,
            "stats": {
              "checkinsCount": 740,
              "usersCount": 424,
              "tipCount": 17
            },
            "url": "http://www.bulkeprzezbibulke.pl",
            "specials": {
              "count": 0,
              "items": []
            },
            "hereNow": {
              "count": 2,
              "summary": "2 people are checked in here",
              "groups": [
                {
                  "type": "others",
                  "name": "Other people here",
                  "count": 2,
                  "items": []
                }
              ]
            },
            "referralId": "v-1426526031"
          },
          {
            "id": "5481c317498ee0762e43d0a6",
            "name": "Bioway",
            "contact": {},
            "location": {
              "address": "Zgoda 3",
              "lat": 52.23265657534626,
              "lng": 21.013826750931553,
              "distance": 13,
              "cc": "PL",
              "city": "Warsaw",
              "state": "Mazowieckie",
              "country": "Poland",
              "formattedAddress": [
                "Zgoda 3",
                "Warsaw",
                "Poland"
              ]
            },
            "categories": [
              {
                "id": "4bf58dd8d48988d1d3941735",
                "name": "Vegetarian / Vegan Restaurant",
                "pluralName": "Vegetarian / Vegan Restaurants",
                "shortName": "Vegetarian / Vegan",
                "icon": {
                  "prefix": "https://ss3.4sqi.net/img/categories_v2/food/vegetarian_",
                  "suffix": ".png"
                },
                "primary": true
              }
            ],
            "verified": false,
            "stats": {
              "checkinsCount": 52,
              "usersCount": 36,
              "tipCount": 5
            },
            "url": "http://bioway.pl",
            "specials": {
              "count": 0,
              "items": []
            },
            "hereNow": {
              "count": 0,
              "summary": "Nobody here",
              "groups": []
            },
            "referralId": "v-1426526031"
          }
        ],
        "confident": true
      }
    }


categories
----------

    https://developer.foursquare.com/categorytree
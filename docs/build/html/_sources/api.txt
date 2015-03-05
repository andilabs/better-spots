API
===

authentication
--------------

.. http:post:: /api/authentication

  :param email: user email
  :param password: user plain text password


**Example request**:

.. sourcecode:: http

    curl -X POST http://dogspot.eu/api/authentication -d "email=andi@andilabs.com&password=somepass"

**Example response**:

.. sourcecode:: http

    {"token": "56a06f4c57817518fdef216fdfd1118250ca069f"}


:statuscode 200: user sucessfully authenticated
:statuscode 401: user UNAUTHORIZED


nearby_spots
------------

.. http:get:: /api/nearby/(float:lat)/(float:lng)/(int:radius)

  :param lat: latitude in exact format: \d{2,3}.\d{5}
  :param lng: longitude in exact format: \d{2,3}.\d{5}
  :param radius: desired radius, if not provided default 5000m will be used

**Example request**:

.. sourcecode:: http

    curl -X GET http://dogspot.eu/api/nearby/52.18654/21.01687/3500

**Example response**:

.. sourcecode:: json

    {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
        {
          "url": "http://dogspot.eu/api/spots/7/",
          "www_url": "http://dogspot.eu/spots/7/jeffs-restaurant-warszawa-zwirki-i-wigory-32/",
          "id": 7,
          "thumbnail_venue_photo": null,
          "distance": 3.3414842332930004,
          "name": "Jeffs",
          "location": {
            "latitude": 52.21104,
            "longitude": 20.98848
          },
          "address_street": "Żwirki i Wigóry",
          "address_number": "32",
          "address_city": "Warszawa",
          "address_country": "Polska",
          "spot_type": 2,
          "is_accepted": true,
          "phone_number": "22 825 16 50",
          "email": "",
          "www": "",
          "facebook": "",
          "is_enabled": false,
          "friendly_rate": "1.00"
        }
      ]
    }

**PAGINATION**

.. http:get:: /api/nearby/(float:lat)/(float:lng)/(int:radius)?page=(int:page_number)

This view uses pagination. If the number of results for given query exeeds the defined in settings MAX_SPOTS_PER_PAGE the pagination will be used. The next parameter will contain link to next page of results.


spots
-----

.. http:get:: /api/spots

    Returns list of all spots.

**Example request**:

.. sourcecode:: http

    curl -X GET http://dogspot.eu/api/spots/

**Example response**:

.. sourcecode:: json

    [
      {
        "url": "http://dogspot.eu/api/spots/2/",
        "www_url": "http://dogspot.eu/spots/2/kafka-cafe-warszawa-obozna-3/",
        "id": 2,
        "thumbnail_venue_photo": null,
        "name": "Kafka",
        "location": {
          "latitude": 52.23959,
          "longitude": 21.02276
        },
        "address_street": "Oboźna",
        "address_number": "3",
        "address_city": "Warszawa",
        "address_country": "Polska",
        "spot_type": 1,
        "is_accepted": true,
        "phone_number": "22 826 08 22",
        "email": "kafka@kafka.com.pl",
        "www": "http://www.kawiarnia-kafka.pl/",
        "facebook": "Kawiarnia.Kafka",
        "is_enabled": true,
        "friendly_rate": "5.00"
      },
      {
        "url": "http://dogspot.eu/api/spots/3/",
        "www_url": "http://dogspot.eu/spots/3/pardon-to-tu-cafe-warszawa-pl-grzybowski-1216/",
        "id": 3,
        "thumbnail_venue_photo": null,
        "name": "Pardon to tu",
        "location": {
          "latitude": 52.23626,
          "longitude": 21.00269
        },
        "address_street": "Pl. Grzybowski",
        "address_number": "12/16",
        "address_city": "Warszawa",
        "address_country": "Polska",
        "spot_type": 1,
        "is_accepted": true,
        "phone_number": "513191641",
        "email": "",
        "www": "http://www.pardontotu.pl/",
        "facebook": "pardontotu",
        "is_enabled": true,
        "friendly_rate": "5.00"
      },
      {
        "url": "http://dogspot.eu/api/spots/1/",
        "www_url": "http://dogspot.eu/spots/1/cafe-kulturalna-cafe-warszawa-plac-defilad-1/",
        "id": 1,
        "thumbnail_venue_photo": null,
        "name": "Cafe Kulturalna",
        "location": {
          "latitude": 52.23177,
          "longitude": 21.00662
        },
        "address_street": "Plac Defilad",
        "address_number": "1",
        "address_city": "Warszawa",
        "address_country": "Polska",
        "spot_type": 1,
        "is_accepted": true,
        "phone_number": "22 656 62 81",
        "email": "justyna@kulturalna.pl",
        "www": "http://www.kulturalna.pl/",
        "facebook": "CafeKulturalna",
        "is_enabled": true,
        "friendly_rate": "3.00"
      }
    ]

.. http:post:: /api/spots

    Add new spot.

    :reqheader Authorization: must provide token to authenticate or be session authenticated
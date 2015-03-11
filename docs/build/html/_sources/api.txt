API
===



authentication
--------------

.. http:post:: /api/authentication

  :param email: user email
  :param password: user plain text password


**Example CURL request**:

.. sourcecode:: http

    curl -X POST http://127.0.0.1:8000/api/authentication -d "email=andi@andilabs.com&password=somepass"

**Example response**:

.. sourcecode:: http

    {"token": "56a06f4c57817518fdef216fdfd1118250ca069f"}


:statuscode 200: user sucessfully authenticated
:statuscode 401: user UNAUTHORIZED


nearby spots list
-----------------

.. http:get:: /api/nearby/(float:lat)/(float:lng)/(int:radius)

  :param lat: latitude in exact format: \d{2,3}.\d{5}
  :param lng: longitude in exact format: \d{2,3}.\d{5}
  :param radius: desired radius, if not provided default 5000m will be used

**Example CURL request**:

.. sourcecode:: http

    curl -X GET http://127.0.0.1:8000/api/nearby/52.18654/21.01687/3500

**Example response**:

.. sourcecode:: json

    {
      "count": 1,
      "next": null,
      "previous": null,
      "results": [
        {
          "url": "http://127.0.0.1:8000/api/spots/7/",
          "www_url": "http://127.0.0.1:8000/spots/7/jeffs-restaurant-warszawa-zwirki-i-wigory-32/",
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

.. note:: This view uses pagination. If the number of results for given query exeeds the defined in settings MAX_SPOTS_PER_PAGE the pagination will be used. The next parameter will contain link to next page of results. Next page will contain previous filed containg link to previous page.

**Pagination:**

.. http:get:: /api/nearby/(float:lat)/(float:lng)/(int:radius)?page=(int:page_number)


spots list
----------

.. http:get:: /api/spots

    Returns list of all spots.

**Example CURL request**:

.. sourcecode:: http

    curl -X GET http://127.0.0.1:8000/api/spots/

**Example response**:

.. sourcecode:: json

    [
      {
        "url": "http://127.0.0.1:8000/api/spots/2/",
        "www_url": "http://127.0.0.1:8000/spots/2/kafka-cafe-warszawa-obozna-3/",
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
        "url": "http://127.0.0.1:8000/api/spots/3/",
        "www_url": "http://127.0.0.1:8000/spots/3/pardon-to-tu-cafe-warszawa-pl-grzybowski-1216/",
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
        "url": "http://127.0.0.1:8000/api/spots/1/",
        "www_url": "http://127.0.0.1:8000/spots/1/cafe-kulturalna-cafe-warszawa-plac-defilad-1/",
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

add new spot
------------

.. http:post:: /api/spots

    Add new spot.

    required fields:

    :param name: string
    :param point: in form of dictionary {"latitude": dd.ddddd, "longitude": dd.ddddd}

    other fields are optional.

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X POST http://127.0.0.1:8000/api/spots/ -H 'Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a' -H 'Content-Type:application/json' -d '{
          "name": "Some New Spot",
          "location": {
            "latitude": 52.23177,
            "longitude": 21.00662
          },
          "address_street": "Newestreet",
          "address_number": "7",
          "address_city": "Warsaw",
          "address_country": "Poland",
          "spot_type": 1,
          "is_accepted": true,
          "phone_number": "22 000 00 00",
          "email": "foo@bar.com",
          "www": "http://www.foo.bar/",
          "facebook": "FooBarFacebook",
          "facilities": {
            "kids_menu": null,
            "playroom": null,
            "baby_changing": true
          }
        }'

spot
----

.. http:get:: /api/spots/(int:pk)/

    Get single spot details. All nested rating, comments and facilities evaluations.

    **Example CURL request**:

    .. sourcecode:: http

        curl -X GET http://127.0.0.1:8000/api/spots/2/

    **Example response**:

    .. sourcecode:: json

        {
            "url": "http://127.0.0.1:8000/api/spots/8/",
            "www_url": "http://127.0.0.1:8000/spots/8/drukarnia-jazz-club-cafe-krakow-nadwislanska-1/",
            "id": 8,
            "thumbnail_venue_photo": null,
            "location": {
                "latitude": 50.04608,
                "longitude": 19.94929
            },
            "ratings": [
                {
                    "url": "http://127.0.0.1:8000/api/ratings/2/",
                    "is_enabled": true,
                    "friendly_rate": 3,
                    "spot": "http://127.0.0.1:8000/api/spots/8/",
                    "user": "http://127.0.0.1:8000/api/users/1/",
                    "opinion": null,
                    "facilities": {
                        "kids_menu": null,
                        "playroom": "False",
                        "baby_changing": "True"
                    }
                },
                {
                    "url": "http://127.0.0.1:8000/api/ratings/4/",
                    "is_enabled": false,
                    "friendly_rate": 5,
                    "spot": "http://127.0.0.1:8000/api/spots/8/",
                    "user": "http://127.0.0.1:8000/api/users/2/",
                    "opinion": null,
                    "facilities": {
                        "kids_menu": "True",
                        "playroom": null,
                        "baby_changing": "False"
                    }
                },
                {
                    "url": "http://127.0.0.1:8000/api/ratings/7/",
                    "is_enabled": true,
                    "friendly_rate": 1,
                    "spot": "http://127.0.0.1:8000/api/spots/8/",
                    "user": "http://127.0.0.1:8000/api/users/3/",
                    "opinion": null,
                    "facilities": {
                        "kids_menu": "True",
                        "playroom": "True",
                        "baby_changing": null
                    }
                }
            ],
            "name": "Drukarnia Jazz Club",
            "address_street": "Nadwiślańska",
            "address_number": "1",
            "address_city": "Kraków",
            "address_country": "Polska",
            "spot_type": 1,
            "is_accepted": true,
            "phone_number": "12 656 65 60",
            "email": "drukarnia@drukarniaclub.pl",
            "www": "http://www.drukarniaclub.pl/",
            "facebook": "DrukarniaJazzClub",
            "is_enabled": true,
            "friendly_rate": "3.00",
            "venue_photo": "http://127.0.0.1:8000/media/img/b22d1ba742aa425baa3665ee8eec0f77",
            "cropping_venue_photo": "0,33,620,298",
            "facilities": {
                "playroom": false,
                "toilet_enabled": true,
                "tables_enabled": true,
                "entrance_enabled": true,
                "baby_changing": false,
                "kids_menu": true
            }
        }


delete spot
-----------

.. http:delete:: /api/spots/(int:pk)/

    Delete single spot

    :param pk: pk of spot

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    The user must be admin.

    **Example CURL request**:

    .. sourcecode:: http

        curl -X DELETE http://127.0.0.1:8000/api/spots/13/ -H "Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a"

    **Example response**:

    .. sourcecode:: http

        HTTP/1.0 204 NO CONTENT


update spot
-----------

.. http:put:: /api/spots/(int:pk)/

    Update single spot

    :param pk: pk of spot

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    The user must be admin.

    **Example CURL request**:

    .. sourcecode:: http

         curl -X PUT http://127.0.0.1:8000/api/spots/2/ -H 'Content-Type:application/json' -H 'Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a' -d '{
          "url": "http://127.0.0.1:8000/api/spots/2/ SOME UPDATE",
          "www_url": "http://127.0.0.1:8000/spots/2/kafka-cafe-warszawa-obozowa-3/",
          "id": 2,
          "thumbnail_venue_photo": null,
          "ratings": [],
          "name": "Kafka SOME UPDATE",
          "location": {
            "latitude": 52.23959,
            "longitude": 21.02276
          },
          "address_street": "Oboźna SOME UPDATE",
          "address_number": "3",
          "address_city": "Warszawa SOME UPDATE",
          "address_country": "POLAND SOME UPDATE",
          "spot_type": 1,
          "is_accepted": true,
          "phone_number": "22 826 08 22",
          "email": "kafka@kafka.com.pl",
          "www": "http://www.kawiarnia-kafka.pl/",
          "facebook": "Kawiarnia.Kafka SOME UPDATE",
          "venue_photo": null,
          "cropping_venue_photo": "0,52,458,249",
          "spot_slug": "kafka-cafe-warszawa-obozowa-3"
        }'


image upload
------------

.. http:post:: /api/image_upload/(int:pk)/

    Upload photo for spot

    required fields:

    :param pk: pk of spot
    :param file: image file

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X POST -H "Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a" -F "file=@/Users/andi/Desktop/dog.jpg;type=image/jpeg" http://127.0.0.1:8000/api/image_upload/1/

    **Example response**:

    .. sourcecode:: json

        {"file_url":"/media/img/64ad3bc3f06f45a9abcdd8167608faee.350x150_q85_box-0%2C936%2C2448%2C1985_crop_detail.jpg"}


favourites spots list
---------------------

.. http:get:: /api/favourites_spots/

    Get list of favourites spots for authenticated user

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X GET -H "Authorization: Token f5d7d38342a2c23c2205a660f4e3ff0464b9a882" http://127.0.0.1:8000/api/favourites_spots/


add spot to favourites
----------------------

.. http:post:: /api/favourites_spots/

    Add spot to favourites

    :param spot: pk value of spot

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X POST http://127.0.0.1:8000/api/favourites_spots/ -H 'Content-Type:application/json' -H 'Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a' -d '{"spot_pk":5}'

    **Example response**:

    :statuscode 404: There is no spot with given id

      .. sourcecode:: json

          {"detail":"Not found"}%}

    :statuscode 304: The spot is already in users favourites

      .. sourcecode:: json

          {"detail":"This spot is already in your favourites"}

    :statuscode 201: The spot was sucessfully added to favourites

      .. sourcecode:: json

          {"detail":"Added Pardon to tu to favourites"}


delete spot from favourites
---------------------------

.. http:delete:: /api/favourites_spots/(int:pk)/

    required fields:

    :param pk: pk of favourites item

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X DELETE http://127.0.0.1:8000/api/favourites_spots/38/ -H "Authorization: Token 66445bc0e3a422f377129ddd79e8dd384e4d8a4a"

ratings list
-------------

.. http:get:: /api/ratings/

    returns all ratings

    **Example CURL request**:

    .. sourcecode:: http

        curl -X GET http://127.0.0.1:8000/api/ratings/

    **Example response**:

    .. sourcecode:: json

        [
            {
                "url": "http://127.0.0.1:8000/api/ratings/34/",
                "is_enabled": true,
                "friendly_rate": 4,
                "spot": "http://127.0.0.1:8000/api/spots/6/",
                "spot_pk": 6,
                "facilities": {
                    "snacks": "True",
                    "dedicated_dogs_menu": "False",
                    "fresh_water": null
                }
            },
            {
                "url": "http://127.0.0.1:8000/api/ratings/35/",
                "is_enabled": false,
                "friendly_rate": 1,
                "spot": "http://127.0.0.1:8000/api/spots/6/",
                "spot_pk": 6,
                "facilities": {
                    "snacks": null,
                    "dedicated_dogs_menu": "True",
                    "fresh_water": "False"
                }
            }
        ]

rate spot
---------
.. http:post:: /api/ratings/

    User can rate each spot only once. If user's rating for given spot already exists, we do not't add next rating but update the exisitng one.

    We return the `new_score` which is calculated average rating from all ratings for  rated spot.

    :param spot_pk: pk of spot to be rated
    :param friendly_rate: integer 1-5

    :reqheader Authorization: must provide token to authenticate or be session authenticated

    **Example CURL request**:

    .. sourcecode:: http

        curl -X POST http://127.0.0.1:8000/api/ratings/ -H 'Content-Type:application/json' -H 'Authorization: Token 3a2d9ee2cfaefea6d073a11641c08152db2b9a04' -d '{
          "spot_pk": 6,
          "friendly_rate": 4,
          "is_enabled": true,
          "facilities": {
            "snacks": true,
            "dedicated_dogs_menu": false,
            "fresh_water": null
          }
        }'

    **Example response**:

    :statuscode 404: There is no spot with given id

      .. sourcecode:: json

          {"detail":"Not found"}


    :statuscode 200: sucessfully added new rating or updated the exisitng one

      .. sourcecode:: json

          {"new_score":3.0,"detail":"Rating added!"}

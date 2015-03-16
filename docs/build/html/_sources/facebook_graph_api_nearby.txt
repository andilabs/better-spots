facebook graph API - nearby
===========================


graph api endpoint
------------------

.. http:get:: hhttps://graph.facebook.com

	applies to all method below


nearby search
-------------


	.. http:get:: /v2.2/search?limit=5000&offset=0&type=place&center={LAT},{LNG}&distance={DISTANCE_IN_METERS}&access_token={FB_OAUTH_TOKEN}

	The FB_OAUTH_TOKEN should be obtain on baceknd using `app-id` and `app-secret`.

	returns:

	.. sourcecode:: json

		{
		  "data": [
		    {
		      "category": "Bar",
		      "category_list": [
		        {
		          "id": "165679780146824",
		          "name": "Food & Restaurant"
		        },
		        {
		          "id": "192661127431931",
		          "name": "Wine Bar"
		        }
		      ],
		      "location": {
		        "street": "Zgoda 4",
		        "city": "Warsaw",
		        "state": "",
		        "country": "Poland",
		        "zip": "00-018",
		        "latitude": 52.23268884537,
		        "longitude": 21.014335088617
		      },
		      "name": "Wejman Wine Bar",
		      "id": "512448662192736"
		    },
		    {
		      "category": "Shopping/retail",
		      "category_list": [
		        {
		          "id": "186230924744328",
		          "name": "Clothing Store"
		        }
		      ],
		      "location": {
		        "street": "Chmielna 24",
		        "city": "Warsaw",
		        "state": "",
		        "country": "Poland",
		        "zip": "00-020",
		        "latitude": 52.232405244959,
		        "longitude": 21.013801969468
		      },
		      "name": "PLNY Stolica",
		      "id": "228146637222742"
		    },
		    {
		      "category": "Local business",
		      "category_list": [
		        {
		          "id": "200742186618963",
		          "name": "Vegetarian & Vegan Restaurant"
		        }
		      ],
		      "location": {
		        "street": "Zgoda 3",
		        "city": "Srodmiescie",
		        "state": "",
		        "country": "Poland",
		        "zip": "",
		        "latitude": 52.232696854145,
		        "longitude": 21.013796683086
		      },
		      "name": "Bioway",
		      "id": "597510767062249"
		    }
		  ],
		  "paging": {
		    "next": "https://graph.facebook.com/v2.2/search?limit=5000&offset=5000&type=place&center=52.2325753,21.013976599999978&distance=50&access_token=1553961588210538|d5ZDNug1oSb8tZ-4TDfv0mykG2I&__after_id=enc_AdDcZB3Dfl2st8ZAB1ZA3hbsmHFhDZB6NT20bDIXH3RoaDKRZB1aAwUZBBZC7rArdKssu0Jiyfci1RS71khaH9uK0dIh9VD"
		  }
		}
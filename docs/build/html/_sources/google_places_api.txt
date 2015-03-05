Google Places API
=================

places API endpoint
-------------------

.. http:get:: https://maps.googleapis.com/maps/api/place

	applies to all method below

	GOOGLE API KEY is mandatory for all below methods


places nearby search
--------------------

.. http:get:: /search/json?location={lat},{lng}&radius={radius_in_meters}&types={type}&sensor=false&key={GOOGLE_API_KEY}&pagetoken={optional_next_page_token}

	you specify users latitude and longitude and desired radius and types of place to be searched.

	Google returns up to 20 results for one request, and if there are more than 20 results the token for fetching next page of results. But API will never return more than 60 results in total.

	Be aware of:

		| short delay between when a next_page_token is issued, and when it will become valid.


	more: https://developers.google.com/places/documentation/search

place detail
------------

.. http:get:: /details/json?placeid={GOOGLE_PLACEID}={GOOGLE_API_KEY}

	more: https://developers.google.com/places/documentation/details

place photo
------------

.. http:get:: /photo?maxwidth={MAX_WIDTH}&photoreference={GOOGLE_PHOTO_REFERENCE}&key={GOOGLE_API_KEY}

	you have specify maxwidth or maxheight

	more: https://developers.google.com/places/documentation/photos
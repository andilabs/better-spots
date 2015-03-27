
foursquare_url = (
    "https://api.foursquare.com/v2/venues/"
    "search?ll={lat},{lng}&client_id={CLEINT_ID}&"
    "client_secret={CLIENT_SECRET}&v=20150316").format(
        lat=1,
        lng=2,
        CLEINT_ID=2,
        CLIENT_SECRET=5
)


google_url = (
    "https://maps.googleapis.com/maps/api/place/search/json?"
    "location={lat},{lng}&radius={radius_in_meters}&types={type}&"
    "sensor=false&key={GOOGLE_API_KEY}&pagetoken={optional_next_page_token}").format(
        lat=1,
        lng=2,
        radius_in_meters=8,
        type=8,
        GOOGLE_API_KEY=9,
        optional_next_page_token=None,
)
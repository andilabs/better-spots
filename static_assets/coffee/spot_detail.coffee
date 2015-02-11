
$ ->
    $("#map_canvas_spot_detail").gmap({'scrollwheel':false}).bind "init", (evt, map) ->

    $("#map_canvas_spot_detail").gmap "addMarker",
        position: new google.maps.LatLng(
            LAT,
            LON
        )
        bounds: true
    $("#map_canvas_spot_detail").gmap "option", "zoom", 17


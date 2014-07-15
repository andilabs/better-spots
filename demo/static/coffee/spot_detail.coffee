


$ ->


   $("#map_canvas_spot_detail").gmap().bind "init", (evt, map) ->

    $("#map_canvas_spot_detail").gmap "addMarker",
      position: new google.maps.LatLng(
        LAT,
        LON
      )
      bounds: true
      dogs_allowed: ['lapka']
      spot_type: ['lapka']
      icon:
        url: STATIC_URL + 'lapka_icon.png',
        size: new google.maps.Size(50,50)

    $("#map_canvas_spot_detail").gmap "option", "zoom", 17
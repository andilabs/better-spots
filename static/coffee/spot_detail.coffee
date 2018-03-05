
$ ->

    $('span.rating').raty
        size: 24
        scoreName: 'friendly_rate'
        starOff: STATIC_URL+'star-off-big.png'
        starHalf: STATIC_URL+'star-half-big.png'
        starOn: STATIC_URL+'star-on-big.png'
        score: ->
            $(this).attr 'data-score'
        readOnly: ->
            !window.isAuthenticated

    $("#map_canvas_spot_detail").gmap({'scrollwheel':false}).bind "init", (evt, map) ->

        $("#map_canvas_spot_detail").gmap "addMarker",
          position: new google.maps.LatLng(LAT,LON)
          bounds: true

        $("#map_canvas_spot_detail").gmap "option", "zoom", 17


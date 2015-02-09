


$ ->
  $("div.rate").raty
    readOnly: false
    score: 0
    # size: 24
    # single   : true
    # starOff : 'star-off-big.png'
    # starOn  : 'star-on-big.png'

   $("#map_canvas_spot_detail").gmap({'scrollwheel':false}).bind "init", (evt, map) ->

    $("#map_canvas_spot_detail").gmap "addMarker",
      position: new google.maps.LatLng(
        LAT,
        LON
      )
      bounds: true
      dogs_allowed: ['lapka']
      spot_type: ['lapka']
      # icon:
      #   url: STATIC_URL + 'lapka_icon.png',
      #   size: new google.maps.Size(50,50)

    $("#map_canvas_spot_detail").gmap "option", "zoom", 17

    $("#dgos_allowance").on "click", (e) ->
      console.log "fired"
      $(@).find('.allowance').each ->
        if $(@).prop('checked') is false
          $(@).parent().css('opacity','0.2')

        else
          $(@).parent().css('opacity','1')


opts =
  lines: 13
  length: 29
  width: 10
  radius: 26
  corners: 0.7
  rotate: 0
  direction: 1
  color: "#000"
  speed: 1.6
  trail: 72
  shadow: false
  hwaccel: false
  className: "spinner"
  zIndex: 2e9
  top: "300%"
  left: "50%"


user_loc_set = false

arrMarkers = {}

filters =
    "dog_allowed": true
    "dog_undefined_allowed": true
    "dog_not_allowed": true
    "caffe": true
    "restaurant": true
    "veterinary_care": true



check_cookies = ->
  for k,v of filters
    if $.cookie(k)
      filters[k] = $.cookie(k)



successFunction = (position) ->
  lat = position.coords.latitude
  long = position.coords.longitude
  console.log "successFunction"
  $.cookie('dogspot_user_lat',lat, {path: '/', expires: 1})
  $.cookie('dogspot_user_long', long, {path: '/', expires: 1})
  r.resolve()


errorFunction = (error) ->
  errors =
    1: 'Permission denied'
    2: 'Position unavailable'
    3: 'Request timeout'

  alert("Error: " + errors[error.code]);
  console.log "thats an error whwhwhahahah", errors[error]


updateGeo = ->
  r = $.Deferred()
  timeoutVal = 10 * 1000 * 1000
  if navigator.geolocation
    navigator.geolocation.getCurrentPosition(successFunction, errorFunction, { enableHighAccuracy: true, timeout: timeoutVal, maximumAge: 0 })
  else
    alert('It seems like Geolocation is disabled')

  r

$ ->
  check_cookies()


  if not $.cookie('dogspot_user_lat') or not $.cookie('dogspot_user_long')
    console.log "nie ma ciasteczek :("
    updateGeo()

  target = document.getElementById("spots_list")
  spinner = new Spinner(opts).spin(target)


  $("#map_filters_button")
    .popover
      trigger: "click"
      placement: "bottom"
      html: true
      title: "Setup your filters:"
      content: "<div id='map_filters'><label class='dog_allowed'>
                <input class='map_filter' type='checkbox' name='dog_allowed' ></label>
                <label class='dog_undefined_allowed'>
                <input class='map_filter' type='checkbox' name='dog_undefined_allowed' ></label>
                <label class='dog_not_allowed'>
                <input class='map_filter'type='checkbox' name='dog_not_allowed' ></label></div>"


  $(document).on 'click', '#map_filters_button', (e) ->
    $("#map_filters input.map_filter").each ->
      ciacho = $.cookie($(@).attr('name'))

      if ciacho and ciacho == "true"
        $(@).prop('checked', ciacho)

  $(document).on 'change', '#map_filters input.map_filter', (e) ->

    $.cookie($(@).attr('name'), $(@).prop('checked'), {path: '/map', expires: 1})



  $("#map_canvas").gmap().bind "init", (evt, map) ->

    if not $.cookie('dogspot_user_lat') or not $.cookie('dogspot_user_long')
      updateGeo().done(successFunction)


    console.log "map!!!---->", $.cookie('dogspot_user_lat'), $.cookie('dogspot_user_long')

    clientPosition = new google.maps.LatLng(
      $.cookie('dogspot_user_lat'),
      $.cookie('dogspot_user_long')
    )


    $("#map_canvas").gmap "addMarker",
      position: clientPosition
      bounds: true
      icon:
        url: STATIC_URL + 'lapka_icon.png',
        size: new google.maps.Size(50,50)



    url = STATIC_URL + "spots_mockup.json"

    jqxhr = $.getJSON url, (datax) ->

      $.each datax, (i, marker) ->

        box = $("<span class='list-group-item' id='#{marker.id}'>
              <h4 class='list-group-item-heading'>#{marker.name}</h4>
              <p class='list-group-item-text'>#{marker.address_street} #{marker.address_number}
              <span class='spot_item_details' id='#{marker.id}'>
              <br><span class='glyphicon glyphicon-phone-alt'></span>
              #{marker.phone_number} <a href='http://www.facebook.com/#{marker.id}'><i class='fa fa-facebook'></i></a>
              </span>
              </p></span>").data("markerek", marker)

        $("#spots_list").append box


        rating_stars = $("<div class='rate'></div>")
            .raty
              readOnly: true
              score: marker.friendly_rate

        contentOfInfoWindow = $("<div class='spot_info' id='#{marker.id}'>
                      <h4>#{marker.name}</h4><br>
                      #{marker.address_street} #{marker.address_number}</div>")
            .append(rating_stars)[0]



        marker.dogs_allowed = "dog_undefined_allowed"  if marker.is_accepted is false

        icony_allowed =
          true: STATIC_URL + "dog_allowed.png"
          false: STATIC_URL + "dog_not_allowed.png"
          dog_undefined_allowed: STATIC_URL + "dog_undefined_allowed.png"
        # console.log marker.dogs_allowed
        SpotIcon = new google.maps.MarkerImage(
          icony_allowed[marker.dogs_allowed],
          null,
          new google.maps.Point(0, 0),
          new google.maps.Point(0, 0)
        )

        SpotMarker = new google.maps.Marker(
          position: new google.maps.LatLng(marker.latitude, marker.longitude)
          bounds: false
          dogs: [marker.dogs_allowed]
          icon: SpotIcon
        )

        SpotInfoWindow = new google.maps.InfoWindow(content: contentOfInfoWindow)

        arrMarkers[marker.id] =
          marker: SpotMarker
          info_window: SpotInfoWindow

        $("#map_canvas").gmap("addMarker", SpotMarker).click ->

          $("#map_canvas").gmap "openInfoWindow", SpotInfoWindow, @
          $("#map_canvas").gmap("get", "map").panTo @.getPosition()

          id = $(contentOfInfoWindow).attr("id")
          $("#spots_list span").not("##{id}").removeClass "active"
          $("#spots_list").find("##{id}").addClass "active"

          $("#spots_list").scrollTop( $("#spots_list").scrollTop() + $("#spots_list").find("##{id}").position().top)


          

          # $('#map_canvas').gmap "findMarker", 'marker.dogs_allowed', 'true', (found, marker) ->
          #   console.log found
          #   console.log marker
            # if found
            #   console.log "true"
            #   marker.setVisible(true)
            # else
            #   console.log "false"
            #   marker.setVisible(false)




      spinner.stop()
      $("#map_canvas").gmap "option", "zoom", 15
      $("#map_canvas").animate({"opacity": "1.0"}, "slow")




$("#spots_list").on "click", "span.list-group-item", (evt) ->

  id = $(@).attr("id")
  $("#spots_list span").not("##{id}").removeClass "active"
  $("#spots_list").find("##{id}").addClass "active"

  $("#map_canvas").gmap "openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[id].marker.getPosition()

  $("#spots_list span.list-group-item").each ->
    # console.log $(@).html()
    # console.log $(@).data("markerek").dogs_allowed
    if $(@).data("markerek").dogs_allowed isnt true
      # console.log "hide!"
      $(@).hide()

  $('#map_canvas').gmap 'find', 'markers', { 'property': 'dogs', 'value': [true] }, (marker, found) ->
    # console.log marker
    # console.log found
    marker.setVisible(found)

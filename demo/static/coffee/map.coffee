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


# clientPosition = new google.maps.LatLng(52.524303, 13.408792)

# user_loc_set = false

spot_type_lookup =
  1: 'caffe'
  2: 'restaurant'
  3: 'store'
  4: 'institution'
  5: 'pet store' #google type: pet_store
  6: 'park'
  7: 'bar'
  8: 'art gallery or museum' #google types: art_gallery + museum
  9: 'veterinary care'# google type: veterinary_care
  0: 'hotel'

arrMarkers = {}

filters_allowance =
    "dog_allowed": true
    "dog_undefined_allowed": true
    "dog_not_allowed": true

filters_types =
    "caffe": true
    "restaurant": true
    "veterinary_care": true



check_cookies = ->
  for k,v of filters_allowance
    if $.cookie(k)
      filters_allowance[k] = eval($.cookie(k))

  for k,v of filters_types
    if $.cookie(k)
      filters_types[k] = eval($.cookie(k))


# successFunction = (position) ->
#   lat = position.coords.latitude
#   long = position.coords.longitude
#   $.cookie('dogspot_user_lat',lat, {path: '/', expires: 1})
#   $.cookie('dogspot_user_long', long, {path: '/', expires: 1})
#   clientPosition = new google.maps.LatLng(lat,long)



# errorFunction = (error) ->
#   errors =
#     1: 'Permission denied'
#     2: 'Position unavailable'
#     3: 'Request timeout'

#   alert("Error: " + errors[error.code]);
#   console.log "thats an error whwhwhahahah", errors[error]


# updateGeo = ->

#   if navigator.geolocation
#     navigator.geolocation.getCurrentPosition(successFunction, errorFunction, { enableHighAccuracy: true, timeout: 3000, maximumAge: 0 })

#   else
#     alert('It seems like Geolocation is disabled')


filterSpots = ->
  filtered_allowance = []

  if filters_allowance["dog_not_allowed"] is true
    filtered_allowance.push false

  if filters_allowance["dog_allowed"] is true
    filtered_allowance.push true

  if filters_allowance["dog_undefined_allowed"] is true
    filtered_allowance.push 'dog_undefined_allowed'


  filtered_types = []

  for k,v of filters_types
    if v is true
      console.log "k,v: #{k}, #{v}"
      #for kk,vv of spot_type_lookup when vv == k
      filtered_types.push k#k



  console.log filters_allowance
  console.log "filtered_allowance", filtered_allowance

  console.log filters_types
  console.log "filtered_types", filtered_types

  $('#map_canvas').gmap 'find', 'markers', { 'property': 'dogs_allowed', 'value': filtered_allowance}, (marker, found) ->
    marker.setVisible(found)

  $('#map_canvas').gmap 'find', 'markers', { 'property': 'spot_type', 'value': filtered_types }, (marker, found) ->
    if marker.visible isnt false
      marker.setVisible(found)


  $("#spots_list span.list-group-item").each ->
    # console.log $(@).html()
    console.log $(@).data("markerek").dogs_allowed

    if $(@).data("markerek").dogs_allowed not in filtered_allowance
      $(@).hide()
    else
      $(@).show()


$ ->
  check_cookies()


  # if not $.cookie('dogspot_user_lat') or not $.cookie('dogspot_user_long')
  #   console.log "nie ma ciasteczek :("
  #   updateGeo()

  target = document.getElementById("spots_list")
  spinner = new Spinner(opts).spin(target)


  $("#map_filters_button")
    .popover
      trigger: "click"
      placement: "left"
      html: true
      title: "Setup your filters:"
      content: "<div id='map_filters'><label class='dog_allowed'>
                <input class='map_filter' type='checkbox' name='dog_allowed' ></label>

                <label class='dog_undefined_allowed'>
                <input class='map_filter' type='checkbox' name='dog_undefined_allowed' ></label>

                <label class='dog_not_allowed'>
                <input class='map_filter'type='checkbox' name='dog_not_allowed' ></label><br><br>

                <i class='fa fa-coffee fa-2x'>
                  <input class='map_filter'type='checkbox' name='caffe' ></i>
                <i class='fa fa-cutlery fa-2x'>
                  <input class='map_filter'type='checkbox' name='restaurant' ></i>
                <i class='fa fa-medkit fa-2x'>
                  <input class='map_filter'type='checkbox' name='veterinary_care' ></i><br>


                </div>"


  $(document).on 'click', '#map_filters_button', (e) ->
    $("#map_filters input.map_filter").each ->
      ciacho = $.cookie($(@).attr('name'))

      if ciacho
        if ciacho == "true"
          $(@).prop('checked', ciacho)
      else
        $(@).prop('checked', true) #on init without cookie always checked


  $(document).on 'change', '#map_filters input.map_filter', (e) ->

    $.cookie($(@).attr('name'), $(@).prop('checked'), {path: '/map', expires: 1})
    check_cookies()
    filterSpots()


  $("#map_canvas").gmap().bind "init", (evt, map) ->

    # if not $.cookie('dogspot_user_lat') or not $.cookie('dogspot_user_long')
    #   updateGeo().done(successFunction)


    # console.log "map!!!---->", $.cookie('dogspot_user_lat'), $.cookie('dogspot_user_long')

    # clientPosition = new google.maps.LatLng(
    #   $.cookie('dogspot_user_lat'),
    #   $.cookie('dogspot_user_long')
    # )

    options =
        enableHighAccuracy: true # boolean (default: false)
        timeout: 10000 #  in milliseconds (default: no limit)
        maximumAge: 10000000 #  in milliseconds (default: 0)

    $("#map_canvas").gmap "getCurrentPosition", (position, status, options) ->
      if status is "OK"
        clientPosition = new google.maps.LatLng(
          position.coords.latitude,
          position.coords.longitude
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
          console.log "----->", spot_type_lookup[marker.spot_type]
          SpotMarker = new google.maps.Marker(
            position: new google.maps.LatLng(marker.latitude, marker.longitude)
            bounds: false
            dogs_allowed: [marker.dogs_allowed]
            spot_type: [spot_type_lookup[marker.spot_type]]
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



        filterSpots()
        spinner.stop()
        $("#map_canvas").gmap "option", "zoom", 15
        $("#map_canvas").animate({"opacity": "1.0"}, "slow")


$("#spots_list").on "click", "span.list-group-item", (evt) ->

  id = $(@).attr("id")
  $("#spots_list span").not("##{id}").removeClass "active"
  $("#spots_list").find("##{id}").addClass "active"

  $("#map_canvas").gmap "openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[id].marker.getPosition()




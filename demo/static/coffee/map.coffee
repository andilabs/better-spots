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


spot_type_lookup =
  1: "caffe"
  2: "restaurant"
  3: "store"
  4: "institution"
  5: "pet store" #google type: pet_store
  6: "park"
  7: "bar"
  8: "art gallery or museum" #google types: art_gallery + museum
  9: "veterinary care"# google type: veterinary_care
  0: "hotel"

my_map = null

arrMarkers = {}

filters_allowance =
    "dog_allowed": true
    "dog_undefined_allowed": true
    "dog_not_allowed": true

filters_types =
    "caffe": true
    "restaurant": true
    "veterinary_care": true


desiredRadius = 2000  #in meters

currentMapCenter =
  lat: null
  lng: null


currentZoomLevel = 14


Number::getRatioForZoom = ->
  console.log this
  591657550.5/Math.pow(2,(this-1))


check_cookies = ->

  for k,v of filters_allowance
    if $.cookie(k)
      filters_allowance[k] = eval($.cookie(k))

  for k,v of filters_types
    if $.cookie(k)
      filters_types[k] = eval($.cookie(k))

Number::toRad = ->
  this * (Math.PI / 180)


calculateDistance = (current_lat, current_lng, new_position_lat, new_position_lng) ->
  ###* returns distance in KM between two geoLocations represented by pair (lat, lng)###
  R = 6371
  dLat = (new_position_lat-current_lat).toRad()
  dLon = (new_position_lng-current_lng).toRad()
  current_lat = current_lat.toRad()
  new_position_lat = new_position_lat.toRad()

  a = Math.sin(dLat/2) * Math.sin(dLat/2) +
          Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(current_lat) * Math.cos(new_position_lat)
  c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
  d = R * c


checkIfNewSpotsShouldBeLoaded = (new_position_lat, new_position_lng, user_zoom_level) ->

  [current_lat, current_lng] = [currentMapCenter.lat, currentMapCenter.lng]
  distance = calculateDistance(current_lat, current_lng, new_position_lat, new_position_lng)

  if distance > desiredRadius/1000 or currentZoomLevel != user_zoom_level
    true

  else
    false

checkIfEmpty = ->

  if $("#spots_list span.list-group-item:visible").not("#memo_empty").size() == 0

    box = $("<span class='list-group-item disabled' id='memo_empty'>
            <h4 class='list-group-item-heading'>No spots to show</h4>
            <p class='list-group-item-text'>
            Try using filters to find some spots
            </p></span>")
    if $("#spots_list span#memo_empty").size() == 0
      $("#spots_list").append box

  else

    $("span#memo_empty").remove()

  $("#spots_list span.list-group-item:visible:not(:last-child)")
    .css('border-bottom-right-radius', '0px')
    .css('border-bottom-left-radius', '0px')

  $("#spots_list span.list-group-item:visible")
    .last()
      .css('margin-bottom','0')
      .css('border-bottom-right-radius', '4px')
      .css('border-bottom-left-radius', '4px')


hideAllInfoWindows = ->

  $('#map_canvas').gmap('closeInfoWindow')


filterSpots = ->

  filtered_allowance = ['lapka']

  if filters_allowance["dog_not_allowed"] is true
    filtered_allowance.push false

  if filters_allowance["dog_allowed"] is true
    filtered_allowance.push true

  if filters_allowance["dog_undefined_allowed"] is true
    filtered_allowance.push 'dog_undefined_allowed'


  filtered_types = ['lapka']

  for k,v of filters_types
    if v is true
      filtered_types.push k


  $('#map_canvas').gmap 'find', 'markers', { 'property': 'dogs_allowed', 'value': filtered_allowance}, (marker, found) ->

    marker.setVisible(found)



  $('#map_canvas').gmap 'find', 'markers', { 'property': 'spot_type', 'value': filtered_types }, (marker, found) ->

    if marker.visible isnt false
      marker.setVisible(found)

    hideAllInfoWindows()


  $("#spots_list span.list-group-item").not("#memo_empty").each ->

      if $(@).data("markerek").dogs_allowed not in filtered_allowance or
      spot_type_lookup[$(@).data("markerek").spot_type] not in [k for k,v of filters_types when v is true][0]
        $(@).hide()

      else
        $(@).show()


switchColumsClasses = (left, right) ->

      $(left)
        .removeClass 'col-md-3'
        .addClass 'col-md-9 no-col-padding'

      $(right)
        .removeClass 'col-md-9 no-col-padding'
        .addClass 'col-md-3'



loadMarkers = (lat, lng) ->
  arrMarkers = {}
  $('#map_canvas').gmap('clear', 'markers')

  target = document.getElementById("right_container")
  spinner = new Spinner(opts).spin(target)

  url = BASE_HOST + "/nearby/#{lat.toFixed(5)}/#{lng.toFixed(5)}/#{desiredRadius}"
  jqxhr = $.getJSON url, (data) ->
  # here we iterate over all the returned markers
    $.each data, (i, marker) ->
      box = $("<span class='list-group-item' id='#{marker.id}'>
            <span class='badge' style='background-color:transparent'>
            <a href='/spots/#{marker.id}' class='spot-details-link disabled' style='color:white'>
            <i class='fa fa-angle-double-right fa-2x'></i></a></span>
            <h4 class='list-group-item-heading'>#{marker.name}</h4>
            <p class='list-group-item-text'>#{marker.address_street}
            #{marker.address_number}
            <span class='spot_item_details' id='#{marker.id}'>
            <br><span class='glyphicon glyphicon-phone-alt'></span>
            #{marker.phone_number} <a href='http://www.facebook.com/#{marker.id}' >
            <i class='fa fa-facebook'></i></a>
            </span>
            </p></span>").data("markerek", marker)


      rating_stars = $("<div class='rate' id='#{marker.id}'></div>")
          .raty
            readOnly: false  #here should be variable from django informing either user is logged in or not
            score: marker.friendly_rate


      contentOfInfoWindow = $("<div class='spot_info' id='#{marker.id}'>
                              <h4>#{marker.name}</h4><br>
                              #{marker.address_street} #{marker.address_number}</div>")
          .append(rating_stars)[0]

      console.log marker.id
      marker.dogs_allowed = "dog_undefined_allowed"  if marker.is_accepted is false

      icony_allowed =
        true: STATIC_URL + "dog_allowed.png"
        false: STATIC_URL + "dog_not_allowed.png"
        dog_undefined_allowed: STATIC_URL + "dog_undefined_allowed.png"
        null: STATIC_URL + "dog_undefined_allowed.png"

      SpotIcon =
        url: icony_allowed[marker.dogs_allowed]
        size: null
        origin: new google.maps.Point(0, 0)
        anchor: new google.maps.Point(0, 0)


      SpotMarker = new google.maps.Marker
        position: new google.maps.LatLng(marker.latitude, marker.longitude)
        bounds: false
        id: marker.id
        dogs_allowed: [marker.dogs_allowed]
        spot_type: [spot_type_lookup[marker.spot_type]]
        icon: SpotIcon


      SpotInfoWindow = new google.maps.InfoWindow
        content: contentOfInfoWindow

      arrMarkers[marker.id] =
        marker: SpotMarker
        info_window: SpotInfoWindow
        box: box








    $("#map_canvas").animate({"opacity": "1.0"}, "slow")
    $("#filters_map_overlay").animate({"opacity": "1.0"}, "slow")


    $("#spots_list").empty()

    for k, marker of arrMarkers
      console.log marker
      $("#spots_list").append marker.box
      $("#map_canvas").gmap("addMarker", marker.marker).click ->
        console.log "blah", @.id
        console.log "blah", arrMarkers[@.id]
        $("#map_canvas").gmap "openInfoWindow", arrMarkers[@.id].info_window, @
        $("#map_canvas").gmap("get", "map").panTo @.getPosition()

        id = @.id #$(contentOfInfoWindow).attr("id")
        $("#spots_list span").not("##{id}").removeClass "active"
        $("#spots_list").find("##{id}").addClass "active"

        $("#spots_list").scrollTop( $("#spots_list").scrollTop() + $("#spots_list").find("##{id}").position().top)



    checkIfEmpty()

  # filterSpots()
  spinner.stop()


$ ->



  filtersFireButton = null

  check_cookies()



  $('body').on 'click', (e) ->
    if $(e.target).parents("#filters_map_overlay").length is 0
      $('#map_filters_button').popover 'hide'


  $("#map_filters_button")
    .popover
      trigger: "click"
      placement: "right"
      html: true
      title: "Setup your filters:"
      content: $("#map_filters").load(STATIC_URL + "filters_popover.html")

    .on 'click', (e) ->
      $("#map_filters").css('display','block')


  $(document).on 'click', '#back_to_list', (e) ->

    $("#spot_detail").remove()

    switchColumsClasses('#right_container', '#left_container')

    filtersFireButton.appendTo("#right_container")

    $("#spots_list").show()
    $("#map_canvas").gmap "option", "zoom", 14
    $('#map_canvas').gmap 'refresh'


  $(document).on 'click', 'a.spot-details-link', (e) ->
    e.preventDefault()
    link = $(@).attr('href')

    $("#spots_list").hide ->
      $('#left_container')
        .append "<div class='list-group'  id='spot_detail'>
          <span class='list-group-item disabled' id='spot_detail_icons'>
          <i class='fa fa-list fa-2x' id='back_to_list'></i></span>
          <span class='list-group-item disabled' id='spot_detail_content'>
          <h4 class='list-group-item-heading'>Spot name</h4>
          <p class='list-group-item-text'>
          #{link}<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
          </p></span>
          </div>"


      filtersFireButton = $("#filters_map_overlay").detach()

      switchColumsClasses('#left_container', '#right_container')

      $("#map_canvas").gmap "option", "zoom", 17
      $('#map_canvas').gmap "refresh"


  $(document).on 'click', '#map_filters_button', (e) ->

    $("#map_filters input.map_filter").each ->

      ciacho = $.cookie($(@).attr('name'))

      if ciacho
        if ciacho == "true"
          $(@).prop('checked', ciacho)
      else
        $(@).prop('checked', true) #on init without cookie always checked

      if $(@).prop('checked') is false
        $(@).parent().css('opacity','0.2')

      else
        $(@).parent().css('opacity','1')


  $(document).on "change", "#map_filters input.map_filter", (e) ->

    if $(@).prop('checked') is false
      $(@).parent().css('opacity','0.2')

    else
      $(@).parent().css('opacity','1')

    $.cookie($(@).attr('name'), $(@).prop('checked'), {path: '/map', expires: 1})

    check_cookies()
    filterSpots()
    checkIfEmpty()


  # here the map is initialized
  $("#map_canvas").gmap({'scrollwheel':false}).bind "init", (evt, map) ->

    options =
        enableHighAccuracy: true # boolean (default: false)
        timeout: 10000 #  in milliseconds (default: no limit)
        maximumAge: 10000000 #  in milliseconds (default: 0)


    # here we get current geo-position of user
    $("#map_canvas").gmap "getCurrentPosition", (position, status, options) ->

      if status is "OK"
        clientPosition = new google.maps.LatLng(
          position.coords.latitude,
          position.coords.longitude
        )
        currentMapCenter.lat = position.coords.latitude
        currentMapCenter.lng = position.coords.longitude
      # here we set icon showing user current location
      $("#map_canvas").gmap "addMarker",
        position: clientPosition
        bounds: true
        dogs_allowed: ['lapka']
        spot_type: ['lapka']
        icon:
          url: STATIC_URL + 'lapka_icon.png',
          size: new google.maps.Size(50,50)

      # here we prepare url and make call for markers


      loadMarkers(clientPosition.lat(), clientPosition.lng())
      $("#map_canvas").gmap "option", "zoom", 14





$("#map_canvas").on 'click', (e) ->
  new_position =  $('#map_canvas').gmap('get','map').getCenter()
  user_zoom_level = $('#map_canvas').gmap('get','map').getZoom()
  console.log $('#map_canvas').gmap('get','map').getZoom()

  if checkIfNewSpotsShouldBeLoaded(new_position.lat(), new_position.lng(), user_zoom_level)
    currentMapCenter.lat = new_position.lat()
    currentMapCenter.lng = new_position.lng()
    currentZoomLevel = $('#map_canvas').gmap('get','map').getZoom()
    desiredRadius =  Math.floor(currentZoomLevel.getRatioForZoom()/10/2)
    loadMarkers(new_position.lat(), new_position.lng())


  console.log "currentZoomLevel", currentZoomLevel
  console.log "radius:", desiredRadius



$("#map_canvas").on 'click', 'div.rate', (e) ->
    #here should happen POST with rating for spot given by logged-in user.
    console.log "spot: #{@.id}"
    console.log $(@).find('input[name="score"]').val()


$("#spots_list").on "click", "span.list-group-item:not(#memo_empty)", (evt) ->

  id = $(@).attr("id")
  $("#spots_list span").not("##{id}").removeClass "active"
  $("#spots_list").find("##{id}").addClass "active"
  $("#spots_list").find("##{id}").find('a.spot-details-link').removeClass('disabled')

  $("#map_canvas").gmap "openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[id].marker.getPosition()


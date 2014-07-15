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
    # .css('margin-bottom','0')
    # .css('margin-top', '0')
    .css('border-bottom-right-radius', '0px')
    .css('border-bottom-left-radius', '0px')

  $("#spots_list span.list-group-item:visible")
    .last()
      .css('margin-bottom','0')
      # .css('margin-top', '0')
      .css('border-bottom-right-radius', '4px')
      .css('border-bottom-left-radius', '4px')

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
    # if marker.visible is false
    #   console.log marker
    #   console.log arrMarkers[marker.id]
    #   iw = arrMarkers[marker.id].info_window
    #   #iwo =  $('#map_canvas').gmap('get',iw)
    #   console.log iw
      # iwo.close()
      #Iw = arrMarkers[marker.id].info_window
      # console.log "closing---->", arrMarkers[marker.id].info_window.content
      # $('#map_canvas').gmap('get','iw', arrMarkers[marker.id].info_window).close()
      #console.log iwo
      #iwo.close()

    # it will be cool to NOT hide open window if its marker matches filter ^^
    #hideAllInfoWindows()
    $('#map_canvas').gmap('refresh')



  $('#map_canvas').gmap 'find', 'markers', { 'property': 'spot_type', 'value': filtered_types }, (marker, found) ->

    if marker.visible isnt false
      marker.setVisible(found)

    hideAllInfoWindows()


  $("#spots_list span.list-group-item").not("#memo_empty").each ->

      if $(@).data("markerek").dogs_allowed not in filtered_allowance or spot_type_lookup[$(@).data("markerek").spot_type] not in [k for k,v of filters_types when v is true][0]# is false
        $(@).hide()
      else
        $(@).show()


switchColumsClasses = (left, right) ->

      $(left)
        .removeClass 'col-xs-12 col-sm-3'
        .addClass 'col-xs-12 col-sm-9 no-col-padding'

      $(right)
        .removeClass 'col-xs-12 col-sm-9 no-col-padding'
        .addClass 'col-xs-12 col-sm-3'


$ ->

  filtersFireButton = null

  check_cookies()

  target = document.getElementById("right_container")
  spinner = new Spinner(opts).spin(target)

  $('body').on 'click', (e) ->
    if $(e.target).parents("#filters_map_overlay").length is 0
      $('#map_filters_button').popover 'hide'


  $("#map_filters_button")
    .popover
      trigger: "click"
      placement: "right"
      html: true
      title: "Setup your filters:"
      content: "<div id='map_filters'>
                <label class='dog_allowed' title='allowed ;-)'>
                  <input class='map_filter' type='checkbox' name='dog_allowed' hidden></label>
                <label class='dog_undefined_allowed' title='undefined :-?' >
                  <input class='map_filter' type='checkbox' name='dog_undefined_allowed' hidden></label>
                <label class='dog_not_allowed' ' title='NOT allowed :-('>
                  <input class='map_filter'type='checkbox' name='dog_not_allowed' hidden></label><br><br>
                <label class='fa fa-coffee fa-2x mar-r-5'' title='Coffee'>
                  <input class='map_filter'type='checkbox' name='caffe' hidden></label>
                <label class='fa fa-cutlery fa-2x mar-r-5' title='Food'>
                  <input class='map_filter'type='checkbox' name='restaurant' hidden></label>
                <label class='fa fa-glass fa-2x mar-r-5 title='pub'>
                  <input class='map_filter'type='checkbox' name='pub' hidden></label>
                <label class='fa fa-medkit fa-2x mar-r-5' title='Vet'>
                  <input class='map_filter'type='checkbox' name='veterinary_care' hidden></label><br>
                </div>"

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
    # console.log $(@).hasClass('disabled')
    # if not $(@).hasClass('disabled')
    $("#spots_list").hide ->
      $('#left_container')
        .append "<div class='list-group'  id='spot_detail'>
          <span class='list-group-item disabled' id='spot_detail_icons'>
          <i class='fa fa-list fa-2x' id='back_to_list'></i></span>
          <span class='list-group-item disabled' id='spot_detail_content'>
          <h4 class='list-group-item-heading'>Spot name</h4>
          <p class='list-group-item-text'>
          #{link}
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


  $("#map_canvas").gmap({'scrollwheel':false}).bind "init", (evt, map) ->

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
        dogs_allowed: ['lapka']
        spot_type: ['lapka']
        icon:
          url: STATIC_URL + 'lapka_icon.png',
          size: new google.maps.Size(50,50)



      url = STATIC_URL + "spots_mockup.json"

      jqxhr = $.getJSON url, (datax) ->

        $.each datax, (i, marker) ->

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

          SpotIcon = new google.maps.MarkerImage(
            icony_allowed[marker.dogs_allowed],
            null,
            new google.maps.Point(0, 0),
            new google.maps.Point(0, 0)
          )

          SpotMarker = new google.maps.Marker(
            position: new google.maps.LatLng(marker.latitude, marker.longitude)
            bounds: false
            id: marker.id
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
        $("#map_canvas").gmap "option", "zoom", 14

        $("#map_canvas").animate({"opacity": "1.0"}, "slow")
        $("#filters_map_overlay").animate({"opacity": "1.0"}, "slow")

        checkIfEmpty()


$("#spots_list").on "click", "span.list-group-item:not(#memo_empty)", (evt) ->

  id = $(@).attr("id")
  $("#spots_list span").not("##{id}").removeClass "active"
  $("#spots_list").find("##{id}").addClass "active"
  $("#spots_list").find("##{id}").find('a.spot-details-link').removeClass('disabled')


  $("#map_canvas").gmap "openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[id].marker.getPosition()




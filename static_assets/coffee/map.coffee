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

window.allSpotsDict = {}

currentMapCenter =
    lat: null
    lng: null

currentZoomLevel = 14

window.filters_allowance =
    "is_enabled": true
    "is_not_enabled": true

window.filters_types =
    "caffe": true
    "restaurant": true

minimumDesiredRadius = 100 #in meters
desiredRadius = 2000  #in meters


getIPbasedLocation = () ->
    loc = null
    $.ajax
        type: 'GET'
        dataType: 'json'
        url: 'http://ipinfo.io/json'
        success: (result) ->
            loc = result.loc
        async: false
    return loc


getDesiredRadius = () ->
    if desiredRadius < minimumDesiredRadius
        minimumDesiredRadius
    else
        desiredRadius


Number::getRatioForZoom = ->
    591657550.5/Math.pow(2,(this-1))


checkCookies = ->
    for k,v of filters_allowance
        if $.cookie(k)
            filters_allowance[k] = eval($.cookie(k))

    for k,v of filters_types
        if $.cookie(k)
            filters_types[k] = eval($.cookie(k))


Number::toRad = ->
    this * (Math.PI / 180)


zoomBasedIconScaleRatio = ->
    if currentZoomLevel >= 15
        return 1.0

    if currentZoomLevel >= 12
        return 1.5

    else
        return 2.0


calculateDistance = (current_lat, current_lng, new_position_lat, new_position_lng) ->
    # returns distance in KM between two geoLocations represented by pair (lat, lng)
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
                        Try using filters and zoom out to find some spots
                        </p></span>")
        if $("#spots_list span#memo_empty").size() == 0
            $("#spots_list").append box

    else
        $("span#memo_empty").remove()

    $('#spots_list span.list-group-item')
        .removeClass('dynamic-first')
        .removeClass('dynamic-last')


    $('#spots_list span.list-group-item:visible')
        .first().addClass('dynamic-first')
        .end()
        .last().addClass('dynamic-last')


hideAllInfoWindows = ->
    $('#map_canvas').gmap('closeInfoWindow')


filterSpots = ->
    filtered_allowance = ['current_location']

    if filters_allowance["is_not_enabled"] is true
        filtered_allowance.push false

    if filters_allowance["is_enabled"] is true
        filtered_allowance.push true

    filtered_types = ['current_location']
    (filtered_types.push k for k,v of filters_types when v is true)

    $('#map_canvas').gmap 'find', 'markers', { 'property': 'is_enabled', 'value': filtered_allowance}, (marker, found) ->
        marker.setVisible(found)

    $('#map_canvas').gmap 'find', 'markers', { 'property': 'spot_type', 'value': filtered_types }, (marker, found) ->
        if marker.visible isnt false
            marker.setVisible(found)
        hideAllInfoWindows()

    $("#spots_list span.list-group-item").not("#memo_empty").each ->

        if $(@).data("spot").is_enabled not in filtered_allowance or
        spot_type_lookup[$(@).data("spot").spot_type] not in [k for k,v of filters_types when v is true][0]
            $(@).hide()
        else
            $(@).show()

    checkIfEmpty()

switchColumsClasses = (left, right) ->
    $(left)
        .removeClass 'col-md-3'
        .addClass 'col-md-9 no-col-padding'
    $(right)
        .removeClass 'col-md-9 no-col-padding'
        .addClass 'col-md-3'


renderInfoWindow = (spot, userReadOnly=true) ->
    rating_stars = $("<br><span class='rating via_modal' id='#{spot.id}'></span>")
        .raty
            scoreName: 'friendly_rate'
            readOnly: userReadOnly
            score: spot.friendly_rate

    $("<div class='spot_info no_copy' id='#{spot.id}'>
       <h4>#{spot.name}</h4><br>
       #{spot.address_street} #{spot.address_number}</div>")
        .append(rating_stars)[0]


renderSpotsTableViewCell = (spot) ->
    $("<span class='list-group-item' id='#{spot.id}'>
        <span class='badge' style='background-color:transparent'>
        <a href='#{spot.www_url}' class='spot-details-link' style='display:none;'>
        <i class='fa fa-angle-double-right fa-2x' style='color:white'></i></a></span>
        <h4 class='list-group-item-heading'>#{spot.name}</h4>
        <p class='list-group-item-text'>#{spot.address_street}
        #{spot.address_number}
        <span class='spot_item_details' id='#{spot.id}'>
        <br><span class='glyphicon glyphicon-phone-alt'></span>
        #{spot.phone_number} <a href='http://www.facebook.com/#{spot.facebook}' target='_blank'>
        <i class='fa fa-facebook'></i></a>
        </span>
        </p></span>").data('spot', spot)


activateSpotTableViewCellFor = (id) ->
    $("#spots_list span").not("##{id}").removeClass "active"
    $("#spots_list").find("##{id}").addClass "active"
    $("#spots_list").find('a.spot-details-link').hide()
    $("#spots_list").find("##{id}").find('a.spot-details-link').toggle()
    $("#spots_list").scrollTop( $("#spots_list").scrollTop() + $("#spots_list").find("##{id}").position().top)


loadMarkers = (lat, lng) ->
    target = document.getElementById("right_container")
    spinner = new Spinner(opts).spin(target)

    if lat == undefined or lng == undefined  or lat == null or lng ==null
        [lat, lng] = getIPbasedLocation().split(',')
        [lat, lng] = [Number(lat), Number(lng)]
    currentMapCenter.lat = lat
    currentMapCenter.lng = lng

    #on each load of markers clean allSpotsDict setting it to empty arr
    window.allSpotsDict = {}

    #on each reload clean all markers on map
    $('#map_canvas').gmap('clear', 'markers')

    url = BASE_HOST + "/api/nearby/#{lat.toFixed(5)}/#{lng.toFixed(5)}/#{getDesiredRadius()}"
    jqxhr = $.getJSON url, (data) ->
        $.each data.results, (i, spot) ->

            icony_allowed =
                true: ICON_URL + "marker-ok.png"
                false: ICON_URL + "marker-bad.png"

            SpotIcon =
                url: icony_allowed[spot.is_enabled]
                size: null
                origin: new google.maps.Point(0, 0)
                anchor: new google.maps.Point(10, 0)
                scaledSize: new google.maps.Size(30/zoomBasedIconScaleRatio(), 30/zoomBasedIconScaleRatio())

            SpotMarker = new google.maps.Marker
                position: new google.maps.LatLng(spot.location.latitude, spot.location.longitude)
                bounds: false
                id: spot.id
                is_enabled: [spot.is_enabled]
                spot_type: [spot_type_lookup[spot.spot_type]]
                icon: SpotIcon

            #important id is exact id from django API
            window.allSpotsDict[spot.id] =
                spot: spot
                marker: SpotMarker

        $("#map_canvas, #map_filters_button").animate({"opacity": "1.0"}, "slow")
        $("#spots_list").empty()

        for k, spot of window.allSpotsDict
            $("#spots_list").append renderSpotsTableViewCell(spot.spot)

            $("#map_canvas").gmap("addMarker", spot.marker).click ->
                # @ is marker, marker has id attr which is id of spot
                $("#map_canvas").gmap("get", "map").panTo @getPosition()

                $("#map_canvas")
                    .gmap "openInfoWindow",
                        position: @getPosition()
                        content: renderInfoWindow(allSpotsDict[@id].spot, userReadOnly=!window.isAuthenticated)

                activateSpotTableViewCellFor(@id)

        filterSpots()
        spinner.stop()

$ ->

    checkCookies()

    $('body').on 'click', (e) ->
        if $(e.target).parents("#map_filters").length is 0 and e.target.id isnt "map_filters_button"
            $('#map_filters_button').popover 'hide'


    $("#map_filters_button")
        .popover
            trigger: "click"
            placement: "right"
            html: true
            title: "Setup your filters:"
            content: """<div id='map_filters' class='no_copy'>
                        <label class='is_enabled' title='enabled ;-)'>
                        <input class='map_filter' type='checkbox' name='is_enabled' hidden></label>
                        <label class='is_not_enabled' title='NOT enabled :-('>
                        <input class='map_filter' type='checkbox' name='is_not_enabled' hidden></label><br><br>
                        <label class='fa fa-coffee fa-2x mar-r-5' title='Coffee'>
                        <input class='map_filter' type='checkbox' name='caffe' hidden></label>
                        <label class='fa fa-cutlery fa-2x mar-r-5' title='Food'>
                        <input class='map_filter' type='checkbox' name='restaurant' hidden></label></div>"""


    $(document).on 'click', '#back_to_list', (e) ->
        $("#spot_detail").remove()
        switchColumsClasses('#right_container', '#left_container')
        $("#map_filters_button").show()
        $("#spots_list").show()
        $("#map_canvas").gmap "option", "zoom", 14
        $('#map_canvas').gmap 'refresh'


    # $(document).on 'click', 'a.spot-details-link', (e) ->
    #     $("#map_filters_button").hide()
    #     e.preventDefault()
    #     link = $(@).attr('href')

    #     $("#spots_list").hide ->
    #         $('#left_container')
    #             .append "<div class='list-group'  id='spot_detail'>
    #                 <a href='#' class='list-group-item disabled' id='spot_detail_icons'>
    #                 <i class='fa fa-list fa-2x' id='back_to_list'></i></a>
    #                 <span class='list-group-item disabled' id='spot_detail_content'>
    #                 <h4 class='list-group-item-heading'>Spot name</h4>
    #                 <p class='list-group-item-text'>
    #                 #{link}<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    #                 </p></span>
    #                 </div>"

    #         switchColumsClasses('#left_container', '#right_container')

            # $("#map_canvas").gmap "option", "zoom", 17
            # $('#map_canvas').gmap "refresh"


    $(document).on 'click', '#map_filters_button', (e) ->
        # RESTORE state of filters from cookies
        $("#map_filters input.map_filter").each ->
            theCookie = $.cookie($(@).attr('name'))
            if theCookie
                if theCookie == "true"
                    $(@).prop('checked', theCookie)
            else
                $(@).prop('checked', true) #on init without cookie always checked

            $(@).parent().css('opacity', if $(@).prop('checked') is false then '0.2' else '1')



    $(document).on "change", "#map_filters input.map_filter", (e) ->
        $(@).parent().css('opacity', if $(@).prop('checked') is false then '0.2' else '1')
        # set cookies to represent current state of filters
        $.cookie($(@).attr('name'), $(@).prop('checked'), {path: '/map', expires: 1})
        checkCookies()
        filterSpots()

    $("#map_canvas").gmap({'scrollwheel':false}).bind "init", (evt, map) ->
        # here the map is initialized
        # https://developer.mozilla.org/en-US/docs/Web/API/PositionOptions
        options =
            enableHighAccuracy: true # boolean (default: false)
            timeout: 10000 #  in milliseconds (default: no limit)
            maximumAge: 10000000 #  in milliseconds (default: 0)

        # here we get current geo-position of user
        $("#map_canvas").gmap "getCurrentPosition", (position, status, options) ->

            if status is "OK"
                clientPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude)

            if clientPosition
                loadMarkers(clientPosition.lat(), clientPosition.lng())
            else
                loadMarkers(null, null)

            # here we set icon showing user current location
            $("#map_canvas")
                .gmap "addMarker",
                    position: new google.maps.LatLng(currentMapCenter.lat, currentMapCenter.lng)
                    bounds: true
                    is_enabled: ['current_location']
                    spot_type: ['current_location']

            $("#map_canvas").gmap "option", "zoom", 14


    $("#map_canvas").on 'click', (e) ->
        new_position =  $('#map_canvas').gmap('get','map').getCenter()
        user_zoom_level = $('#map_canvas').gmap('get','map').getZoom()

        if checkIfNewSpotsShouldBeLoaded(new_position.lat(), new_position.lng(), user_zoom_level)
            currentMapCenter.lat = new_position.lat()
            currentMapCenter.lng = new_position.lng()
            currentZoomLevel = $('#map_canvas').gmap('get','map').getZoom()
            desiredRadius =  Math.floor(currentZoomLevel.getRatioForZoom()/10/2)
            loadMarkers(new_position.lat(), new_position.lng())
            clientPosition = new google.maps.LatLng(currentMapCenter.lat, currentMapCenter.lng)


    $("#spots_list").on "click", "span.list-group-item:not(#memo_empty)", (evt) ->
        activateSpotTableViewCellFor(@id)

        $("#map_canvas")
            .gmap "openInfoWindow",
                position: window.allSpotsDict[@id].marker.getPosition()
                content: renderInfoWindow(allSpotsDict[@id].spot, userReadOnly=!window.isAuthenticated)

        $("#map_canvas").gmap("get", "map").panTo window.allSpotsDict[@id].marker.getPosition()

    # $("#map_canvas").on 'click', 'div.rating via_modal', (e) ->
    #     #here should happen POST with rating for spot given by logged-in user.
    #     console.log "spot: #{@.id} score: #{$(@).find('input[name="score"]').val()}"
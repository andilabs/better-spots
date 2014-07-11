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





arrMarkers = {}

$ ->

  target = document.getElementById("spots_list")
  spinner = new Spinner(opts).spin(target)


  $("#map_canvas").gmap().bind "init", (evt, map) ->

    $("#map_canvas").gmap "getCurrentPosition", (position, status) ->

      if status is "OK"

        clientPosition = new google.maps.LatLng(
          position.coords.latitude,
          position.coords.longitude
          )

        ikonka = new google.maps.MarkerImage(
          "http://127.0.0.1:8000/static/lapka_icon.png",
          new google.maps.Size(50, 50),
          new google.maps.Point(0, 0),
          new google.maps.Point(0, 50)
          )

        $("#map_canvas").gmap "addMarker",
          position: clientPosition
          bounds: true
          icon: ikonka

        .click ->
          $("#map_canvas").gmap "openInfoWindow",
            content: "<h2>You!</h2>"

      else

        $("#map_canvas").gmap "option", "zoom", 3


      pair_mark = {}

      url = "http://127.0.0.1:8000/static/spots_mockup.json"

      jqxhr = $.getJSON(url, (data) ->

        $.each data, (i, marker) ->

          box = "<a href='#' class='list-group-item' id='#{marker.id}'>
                <h4 class='list-group-item-heading'>#{marker.name}</h4>
                <p class='list-group-item-text'>#{marker.address_street} #{marker.address_number}
                <span class='spot_item_details' style='display:none' id='#{marker.id}'>
                <br><span class='glyphicon glyphicon-phone-alt'></span>
                #{marker.phone_number} <i class='fa fa-facebook'></i>
                </span>
                </p></a>"

          $("#spots_list").append box

          labelka = '#spot#{marker.id}'

          contencik = $("<div class='spot_info' id='#{marker.id}'><h4>#{marker.name}</h4><br>#{marker.address_street} #{marker.address_number}</div>")
            .append(
              $("<div id='spot#{marker.id}' class='rate'></div>")
              .raty(
                readOnly: true
                score: marker.friendly_rate
              ))[0]

          pair_mark[labelka] = marker.friendly_rate

          marker.dogs_allowed = "dog_undefined_allowed"  if marker.is_accepted is false

          icony_allowed =
            true: "http://127.0.0.1:8000/static/dog_allowed.png"
            false: "http://127.0.0.1:8000/static/dog_not_allowed.png"
            dog_undefined_allowed: "http://127.0.0.1:8000/static/dog_undefined_allowed.png"

          SpotIcon = new google.maps.MarkerImage(
            icony_allowed[marker.dogs_allowed],
            null,
            new google.maps.Point(0, 0),
            new google.maps.Point(0, 0)
            )

          SpotMarker = new google.maps.Marker(
            position: new google.maps.LatLng(marker.latitude, marker.longitude)
            bounds: false
            icon: SpotIcon
          )

          SpotInfoWindow = new google.maps.InfoWindow(content: contencik)

          arrMarkers[marker.id] =
            marker: SpotMarker
            info_window: SpotInfoWindow

          $("#map_canvas").gmap("addMarker", SpotMarker).click ->

            $("#map_canvas").gmap "openInfoWindow", SpotInfoWindow, @
            $("#map_canvas").gmap("get", "map").panTo @getPosition()
            idik = "#" + $(contencik).attr("id")

            $("#spots_list a").each (index) ->

              $(@).removeClass "active"
              $(@).find("p span.spot_item_details").attr "style", "display:none"

            $("#spots_list").find(idik).focus().attr "class", "list-group-item active"
            $("#spots_list p").find("span#{idik}").attr "style", "display:block")

      spinner.stop()
      $("#map_canvas").animate({"opacity": "1.0"}, "slow")
      $("#map_canvas").gmap "option", "zoom", 15


$("#spots_list").on "click", "a.list-group-item", (evt) ->

  $("#spots_list a").each (index) ->

    $(@).removeClass "active"
    $(@).find("p span.spot_item_details").attr "style", "display:none"

  idik = $(@).attr("id")
  $("#spots_list").find("#" + idik).focus().attr "class", "list-group-item active"
  $("#spots_list p").find("span#" + idik).attr "style", "display:block"
  $("#map_canvas").gmap "openInfoWindow", arrMarkers[idik].info_window, arrMarkers[idik].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[idik].marker.getPosition()


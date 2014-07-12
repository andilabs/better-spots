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


        $("#map_canvas").gmap "addMarker",
          position: clientPosition
          bounds: true
          icon:
            url: STATIC_URL + 'lapka_icon.png',
            size: new google.maps.Size(50,50)



      url = STATIC_URL + "spots_mockup.json"

      jqxhr = $.getJSON(url, (data) ->

        $.each data, (i, marker) ->

          box = "<span class='list-group-item' id='#{marker.id}'>
                <h4 class='list-group-item-heading'>#{marker.name}</h4>
                <p class='list-group-item-text'>#{marker.address_street} #{marker.address_number}
                <span class='spot_item_details' id='#{marker.id}'>
                <br><span class='glyphicon glyphicon-phone-alt'></span>
                #{marker.phone_number} <a href='http://www.facebook.com/#{marker.id}'><i class='fa fa-facebook'></i></a>
                </span>
                </p></span>"

          $("#spots_list").append box


          rating_stars = $("<div class='rate'></div>")
              .raty
                readOnly: true
                score: marker.friendly_rate

          contencik = $("<div class='spot_info' id='#{marker.id}'>
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
            icon: SpotIcon
          )

          SpotInfoWindow = new google.maps.InfoWindow(content: contencik)

          arrMarkers[marker.id] =
            marker: SpotMarker
            info_window: SpotInfoWindow

          $("#map_canvas").gmap("addMarker", SpotMarker).click ->

            $("#map_canvas").gmap "openInfoWindow", SpotInfoWindow, @
            $("#map_canvas").gmap("get", "map").panTo @.getPosition()

            id = "##{$(contencik).attr("id")}"

            $("#spots_list span").each (index) ->

              $(@).removeClass "active"

            $("#spots_list").scrollTop( $("#spots_list").scrollTop() + $("#spots_list").find(id).position().top);
            $("#spots_list").find(id).attr "class", "list-group-item active"

            )

      spinner.stop()
      $("#map_canvas").gmap "option", "zoom", 15
      $("#map_canvas").animate({"opacity": "1.0"}, "slow")



$("#spots_list").on "click", "span.list-group-item", (evt) ->

  $("#spots_list span").each (index) ->

    $(@).removeClass "active"


  id = $(@).attr("id")

  $("#spots_list").find("##{id}").attr "class", "list-group-item active"
  $("#map_canvas").gmap "openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker
  $("#map_canvas").gmap("get", "map").panTo arrMarkers[id].marker.getPosition()


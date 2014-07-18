// Generated by CoffeeScript 1.7.1
(function() {
  var arrMarkers, checkIfEmpty, check_cookies, filterSpots, filters_allowance, filters_types, hideAllInfoWindows, my_map, opts, spot_type_lookup, switchColumsClasses,
    __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  opts = {
    lines: 13,
    length: 29,
    width: 10,
    radius: 26,
    corners: 0.7,
    rotate: 0,
    direction: 1,
    color: "#000",
    speed: 1.6,
    trail: 72,
    shadow: false,
    hwaccel: false,
    className: "spinner",
    zIndex: 2e9
  };

  spot_type_lookup = {
    1: "caffe",
    2: "restaurant",
    3: "store",
    4: "institution",
    5: "pet store",
    6: "park",
    7: "bar",
    8: "art gallery or museum",
    9: "veterinary care",
    0: "hotel"
  };

  my_map = null;

  arrMarkers = {};

  filters_allowance = {
    "dog_allowed": true,
    "dog_undefined_allowed": true,
    "dog_not_allowed": true
  };

  filters_types = {
    "caffe": true,
    "restaurant": true,
    "veterinary_care": true
  };

  check_cookies = function() {
    var k, v, _results;
    for (k in filters_allowance) {
      v = filters_allowance[k];
      if ($.cookie(k)) {
        filters_allowance[k] = eval($.cookie(k));
      }
    }
    _results = [];
    for (k in filters_types) {
      v = filters_types[k];
      if ($.cookie(k)) {
        _results.push(filters_types[k] = eval($.cookie(k)));
      } else {
        _results.push(void 0);
      }
    }
    return _results;
  };

  checkIfEmpty = function() {
    var box;
    if ($("#spots_list span.list-group-item:visible").not("#memo_empty").size() === 0) {
      box = $("<span class='list-group-item disabled' id='memo_empty'> <h4 class='list-group-item-heading'>No spots to show</h4> <p class='list-group-item-text'> Try using filters to find some spots </p></span>");
      if ($("#spots_list span#memo_empty").size() === 0) {
        $("#spots_list").append(box);
      }
    } else {
      $("span#memo_empty").remove();
    }
    $("#spots_list span.list-group-item:visible:not(:last-child)").css('border-bottom-right-radius', '0px').css('border-bottom-left-radius', '0px');
    return $("#spots_list span.list-group-item:visible").last().css('margin-bottom', '0').css('border-bottom-right-radius', '4px').css('border-bottom-left-radius', '4px');
  };

  hideAllInfoWindows = function() {
    return $('#map_canvas').gmap('closeInfoWindow');
  };

  filterSpots = function() {
    var filtered_allowance, filtered_types, k, v;
    filtered_allowance = ['lapka'];
    if (filters_allowance["dog_not_allowed"] === true) {
      filtered_allowance.push(false);
    }
    if (filters_allowance["dog_allowed"] === true) {
      filtered_allowance.push(true);
    }
    if (filters_allowance["dog_undefined_allowed"] === true) {
      filtered_allowance.push('dog_undefined_allowed');
    }
    filtered_types = ['lapka'];
    for (k in filters_types) {
      v = filters_types[k];
      if (v === true) {
        filtered_types.push(k);
      }
    }
    $('#map_canvas').gmap('find', 'markers', {
      'property': 'dogs_allowed',
      'value': filtered_allowance
    }, function(marker, found) {
      return marker.setVisible(found);
    });
    $('#map_canvas').gmap('find', 'markers', {
      'property': 'spot_type',
      'value': filtered_types
    }, function(marker, found) {
      if (marker.visible !== false) {
        marker.setVisible(found);
      }
      return hideAllInfoWindows();
    });
    return $("#spots_list span.list-group-item").not("#memo_empty").each(function() {
      var _ref, _ref1;
      if ((_ref = $(this).data("markerek").dogs_allowed, __indexOf.call(filtered_allowance, _ref) < 0) || (_ref1 = spot_type_lookup[$(this).data("markerek").spot_type], __indexOf.call([
        (function() {
          var _results;
          _results = [];
          for (k in filters_types) {
            v = filters_types[k];
            if (v === true) {
              _results.push(k);
            }
          }
          return _results;
        })()
      ][0], _ref1) < 0)) {
        return $(this).hide();
      } else {
        return $(this).show();
      }
    });
  };

  switchColumsClasses = function(left, right) {
    $(left).removeClass('col-xs-12 col-sm-3').addClass('col-xs-12 col-sm-9 no-col-padding');
    return $(right).removeClass('col-xs-12 col-sm-9 no-col-padding').addClass('col-xs-12 col-sm-3');
  };

  $(function() {
    var desiredRadius, filtersFireButton, spinner, target;
    desiredRadius = 3000;
    filtersFireButton = null;
    check_cookies();
    target = document.getElementById("right_container");
    spinner = new Spinner(opts).spin(target);
    $('body').on('click', function(e) {
      if ($(e.target).parents("#filters_map_overlay").length === 0) {
        return $('#map_filters_button').popover('hide');
      }
    });
    $("#map_filters_button").popover({
      trigger: "click",
      placement: "right",
      html: true,
      title: "Setup your filters:",
      content: $("#map_filters").load(STATIC_URL + "filters_popover.html")
    }).on('click', function(e) {
      return $("#map_filters").css('display', 'block');
    });
    $(document).on('click', '#back_to_list', function(e) {
      $("#spot_detail").remove();
      switchColumsClasses('#right_container', '#left_container');
      filtersFireButton.appendTo("#right_container");
      $("#spots_list").show();
      $("#map_canvas").gmap("option", "zoom", 14);
      return $('#map_canvas').gmap('refresh');
    });
    $(document).on('click', 'a.spot-details-link', function(e) {
      var link;
      e.preventDefault();
      link = $(this).attr('href');
      return $("#spots_list").hide(function() {
        $('#left_container').append("<div class='list-group'  id='spot_detail'> <span class='list-group-item disabled' id='spot_detail_icons'> <i class='fa fa-list fa-2x' id='back_to_list'></i></span> <span class='list-group-item disabled' id='spot_detail_content'> <h4 class='list-group-item-heading'>Spot name</h4> <p class='list-group-item-text'> " + link + " </p></span> </div>");
        filtersFireButton = $("#filters_map_overlay").detach();
        switchColumsClasses('#left_container', '#right_container');
        $("#map_canvas").gmap("option", "zoom", 17);
        return $('#map_canvas').gmap("refresh");
      });
    });
    $(document).on('click', '#map_filters_button', function(e) {
      return $("#map_filters input.map_filter").each(function() {
        var ciacho;
        ciacho = $.cookie($(this).attr('name'));
        if (ciacho) {
          if (ciacho === "true") {
            $(this).prop('checked', ciacho);
          }
        } else {
          $(this).prop('checked', true);
        }
        if ($(this).prop('checked') === false) {
          return $(this).parent().css('opacity', '0.2');
        } else {
          return $(this).parent().css('opacity', '1');
        }
      });
    });
    $(document).on("change", "#map_filters input.map_filter", function(e) {
      if ($(this).prop('checked') === false) {
        $(this).parent().css('opacity', '0.2');
      } else {
        $(this).parent().css('opacity', '1');
      }
      $.cookie($(this).attr('name'), $(this).prop('checked'), {
        path: '/map',
        expires: 1
      });
      check_cookies();
      filterSpots();
      return checkIfEmpty();
    });
    return $("#map_canvas").gmap({
      'scrollwheel': false
    }).bind("init", function(evt, map) {
      var options;
      options = {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 10000000
      };
      return $("#map_canvas").gmap("getCurrentPosition", function(position, status, options) {
        var clientPosition, jqxhr, url;
        if (status === "OK") {
          clientPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        }
        $("#map_canvas").gmap("addMarker", {
          position: clientPosition,
          bounds: true,
          dogs_allowed: ['lapka'],
          spot_type: ['lapka'],
          icon: {
            url: STATIC_URL + 'lapka_icon.png',
            size: new google.maps.Size(50, 50)
          }
        });
        url = BASE_HOST + ("/nearby/" + (clientPosition.lat().toFixed(5)) + "/" + (clientPosition.lng().toFixed(5)) + "/" + desiredRadius);
        return jqxhr = $.getJSON(url, function(datax) {
          $.each(datax, function(i, marker) {
            var SpotIcon, SpotInfoWindow, SpotMarker, box, contentOfInfoWindow, icony_allowed, rating_stars;
            box = $("<span class='list-group-item' id='" + marker.id + "'> <span class='badge' style='background-color:transparent'> <a href='/spots/" + marker.id + "' class='spot-details-link disabled' style='color:white'> <i class='fa fa-angle-double-right fa-2x'></i></a></span> <h4 class='list-group-item-heading'>" + marker.name + "</h4> <p class='list-group-item-text'>" + marker.address_street + " " + marker.address_number + " <span class='spot_item_details' id='" + marker.id + "'> <br><span class='glyphicon glyphicon-phone-alt'></span> " + marker.phone_number + " <a href='http://www.facebook.com/" + marker.id + "' > <i class='fa fa-facebook'></i></a> </span> </p></span>").data("markerek", marker);
            $("#spots_list").append(box);
            rating_stars = $("<div class='rate'></div>").raty({
              readOnly: true,
              score: marker.friendly_rate
            });
            contentOfInfoWindow = $("<div class='spot_info' id='" + marker.id + "'> <h4>" + marker.name + "</h4><br> " + marker.address_street + " " + marker.address_number + "</div>").append(rating_stars)[0];
            if (marker.is_accepted === false) {
              marker.dogs_allowed = "dog_undefined_allowed";
            }
            icony_allowed = {
              "true": STATIC_URL + "dog_allowed.png",
              "false": STATIC_URL + "dog_not_allowed.png",
              dog_undefined_allowed: STATIC_URL + "dog_undefined_allowed.png"
            };
            SpotIcon = new google.maps.MarkerImage(icony_allowed[marker.dogs_allowed], null, new google.maps.Point(0, 0), new google.maps.Point(0, 0));
            SpotMarker = new google.maps.Marker({
              position: new google.maps.LatLng(marker.latitude, marker.longitude),
              bounds: false,
              id: marker.id,
              dogs_allowed: [marker.dogs_allowed],
              spot_type: [spot_type_lookup[marker.spot_type]],
              icon: SpotIcon
            });
            SpotInfoWindow = new google.maps.InfoWindow({
              content: contentOfInfoWindow
            });
            arrMarkers[marker.id] = {
              marker: SpotMarker,
              info_window: SpotInfoWindow
            };
            return $("#map_canvas").gmap("addMarker", SpotMarker).click(function() {
              var id;
              $("#map_canvas").gmap("openInfoWindow", SpotInfoWindow, this);
              $("#map_canvas").gmap("get", "map").panTo(this.getPosition());
              id = $(contentOfInfoWindow).attr("id");
              $("#spots_list span").not("#" + id).removeClass("active");
              $("#spots_list").find("#" + id).addClass("active");
              return $("#spots_list").scrollTop($("#spots_list").scrollTop() + $("#spots_list").find("#" + id).position().top);
            });
          });
          filterSpots();
          spinner.stop();
          $("#map_canvas").gmap("option", "zoom", 14);
          $("#map_canvas").animate({
            "opacity": "1.0"
          }, "slow");
          $("#filters_map_overlay").animate({
            "opacity": "1.0"
          }, "slow");
          return checkIfEmpty();
        });
      });
    });
  });

  $("#spots_list").on("click", "span.list-group-item:not(#memo_empty)", function(evt) {
    var id;
    id = $(this).attr("id");
    $("#spots_list span").not("#" + id).removeClass("active");
    $("#spots_list").find("#" + id).addClass("active");
    $("#spots_list").find("#" + id).find('a.spot-details-link').removeClass('disabled');
    $("#map_canvas").gmap("openInfoWindow", arrMarkers[id].info_window, arrMarkers[id].marker);
    return $("#map_canvas").gmap("get", "map").panTo(arrMarkers[id].marker.getPosition());
  });

}).call(this);

// Generated by CoffeeScript 1.9.0
(function() {
  var activateSpotTableViewCellFor, calculateDistance, checkCookies, checkIfEmpty, checkIfNewSpotsShouldBeLoaded, currentZoomLevel, desiredRadius, filterSpots, geoCode, getDesiredRadius, hideAllInfoWindows, loadMarkers, minimumDesiredRadius, opts, renderInfoWindow, renderSpotsTableViewCell, reverseGeoCode, setCurrenMapCenter, spot_type_lookup, switchColumsClasses, zoomBasedIconScaleRatio,
    __indexOf = [].indexOf || function(item) { for (var i = 0, l = this.length; i < l; i++) { if (i in this && this[i] === item) return i; } return -1; };

  opts = {
    radius: 30,
    corners: 0.7,
    rotate: 0,
    direction: 1,
    color: "#000",
    speed: 2.6,
    trail: 72,
    shadow: false,
    hwaccel: false,
    className: "spinner",
    zIndex: 2e9
  };

  spot_type_lookup = {
    1: "caffe",
    2: "restaurant",
    3: "hotel",
    4: "shop - no food",
    5: "shop - with food"
  };

  window.allSpotsDict = {};

  window.currentMapCenter = {
    latitude: null,
    longitude: null
  };

  window.currentAddress = null;

  window.initialize = function() {
    return reverseGeoCode(function(d) {
      window.currentAddress = d;
      return console.log(d);
    });
  };

  window.initialize2 = function() {
    return geoCode(function(e) {
      return console.log(e);
    });
  };

  reverseGeoCode = function(callback) {
    var geocoder, location;
    location = new google.maps.LatLng(currentMapCenter.latitude, currentMapCenter.longitude);
    geocoder = new google.maps.Geocoder();
    if (geocoder) {
      return geocoder.geocode({
        'latLng': location
      }, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
          if (results[1]) {
            return callback(results[1].formatted_address);
          } else {
            return console.log('No results found');
          }
        } else {
          return console.log('Geocoder failed due to: ' + status);
        }
      });
    }
  };

  geoCode = function(callback) {
    var geocoder;
    geocoder = new google.maps.Geocoder();
    if (geocoder) {
      return geocoder.geocode({
        'address': window.currentAddress
      }, function(results, status) {
        if (status === google.maps.GeocoderStatus.OK) {
          if (results[0]) {
            return callback(JSON.stringify(results[0].geometry.location));
          } else {
            return console.log('No results found');
          }
        } else {
          return console.log('Geocode was not successful for the following reason: ' + status);
        }
      });
    }
  };

  setCurrenMapCenter = function(lat, lng) {
    window.currentMapCenter.latitude = lat;
    window.currentMapCenter.longitude = lng;
    return localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter));
  };

  currentZoomLevel = 14;

  window.filters_allowance = {
    "is_enabled": true,
    "is_not_enabled": true
  };

  window.filters_types = {
    "caffe": true,
    "restaurant": true,
    "hotel": true,
    "shop - no food": true,
    "shop - with food": true
  };

  minimumDesiredRadius = 100;

  desiredRadius = 5000;

  getDesiredRadius = function() {
    if (desiredRadius < minimumDesiredRadius) {
      return minimumDesiredRadius;
    } else {
      return desiredRadius;
    }
  };

  Number.prototype.getRatioForZoom = function() {
    return 591657550.5 / Math.pow(2, this - 1);
  };

  checkCookies = function() {
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

  Number.prototype.toRad = function() {
    return this * (Math.PI / 180);
  };

  zoomBasedIconScaleRatio = function() {
    if (currentZoomLevel >= 15) {
      return 1.0;
    }
    if (currentZoomLevel >= 12) {
      return 1.5;
    } else {
      return 2.0;
    }
  };

  calculateDistance = function(currentLat, currentLng, newPositionLat, newPositionLng) {
    var R, a, c, d, dLat, dLon;
    R = 6371;
    dLat = (newPositionLat - currentLat).toRad();
    dLon = (newPositionLng - currentLng).toRad();
    currentLat = currentLat.toRad();
    newPositionLat = newPositionLat.toRad();
    a = Math.sin(dLat / 2) * Math.sin(dLat / 2) + Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(currentLat) * Math.cos(newPositionLat);
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return d = R * c;
  };

  checkIfNewSpotsShouldBeLoaded = function(newPositionLat, newPositionLng, userZoomLevel) {
    var currentLat, currentLng, distance, _ref;
    _ref = [currentMapCenter.latitude, currentMapCenter.longitude], currentLat = _ref[0], currentLng = _ref[1];
    distance = calculateDistance(currentLat, currentLng, newPositionLat, newPositionLng);
    if (distance > desiredRadius / 1000 || currentZoomLevel !== userZoomLevel) {
      return true;
    } else {
      return false;
    }
  };

  checkIfEmpty = function() {
    var box;
    if ($("#spots_list span.list-group-item:visible").not("#memo_empty").size() === 0) {
      box = $("<span class='list-group-item disabled' id='memo_empty'> <h4 class='list-group-item-heading'>No spots to show</h4> <p class='list-group-item-text'> Try using filters and zoom out to find some spots </p></span>");
      if ($("#spots_list span#memo_empty").size() === 0) {
        $("#spots_list").append(box);
      }
    } else {
      $("span#memo_empty").remove();
    }
    $('#spots_list span.list-group-item').removeClass('dynamic-first').removeClass('dynamic-last');
    return $('#spots_list span.list-group-item:visible').first().addClass('dynamic-first').end().last().addClass('dynamic-last');
  };

  hideAllInfoWindows = function() {
    return $('#map_canvas').gmap('closeInfoWindow');
  };

  filterSpots = function() {
    var filtered_allowance, filtered_types, k, v;
    filtered_allowance = ['current_location'];
    if (filters_allowance["is_not_enabled"] === true) {
      filtered_allowance.push(false);
    }
    if (filters_allowance["is_enabled"] === true) {
      filtered_allowance.push(true);
    }
    filtered_types = ['current_location'];
    for (k in filters_types) {
      v = filters_types[k];
      if (v === true) {
        filtered_types.push(k);
      }
    }
    $('#map_canvas').gmap('find', 'markers', {
      'property': 'is_enabled',
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
    $("#spots_list span.list-group-item").not("#memo_empty").each(function() {
      var _ref, _ref1;
      if ((_ref = $(this).data("spot").is_enabled, __indexOf.call(filtered_allowance, _ref) < 0) || (_ref1 = spot_type_lookup[$(this).data("spot").spot_type], __indexOf.call([
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
    return checkIfEmpty();
  };

  switchColumsClasses = function(left, right) {
    $(left).removeClass('col-md-3').addClass('col-md-9 no-col-padding');
    return $(right).removeClass('col-md-9 no-col-padding').addClass('col-md-3');
  };

  renderInfoWindow = function(spot, userReadOnly) {
    var rating_stars;
    if (userReadOnly == null) {
      userReadOnly = true;
    }
    rating_stars = $("<br><span class='rating via_modal' id='" + spot.id + "'></span>").raty({
      scoreName: 'friendly_rate',
      readOnly: userReadOnly,
      score: spot.friendly_rate
    });
    return $("<div class='spot_info no_copy' id='" + spot.id + "'> <h4><a href='" + spot.www_url + "'>" + spot.name + "</a></h4><br> " + spot.address_street + " " + spot.address_number + "</div>").append(rating_stars)[0];
  };

  renderSpotsTableViewCell = function(spot) {
    return $("<span class='list-group-item' id='" + spot.id + "'> <span class='badge' style='background-color:transparent'> <a href='" + spot.www_url + "' class='spot-details-link' style='display:none;'> <i class='fa fa-angle-double-right fa-2x' style='color:white'></i></a></span> <h4 class='list-group-item-heading'>" + spot.name + "</h4> <p class='list-group-item-text'>" + spot.address_street + " " + spot.address_number + " <span class='spot_item_details' id='" + spot.id + "'> " + [spot.phone_number ? "<br><span class='glyphicon glyphicon-phone-alt'></span> " + spot.phone_number : void 0] + " " + [spot.facebook ? "<br><a href='http://www.facebook.com/" + spot.facebook + "' target='_blank'> <i class='fa fa-facebook'></i> " + (spot.facebook.substring(0, 15)) + "</a>" : void 0] + " </span> </p></span>").data('spot', spot);
  };

  activateSpotTableViewCellFor = function(id) {
    $("#spots_list span").not("#" + id).removeClass("active");
    $("#spots_list").find("#" + id).addClass("active");
    $("#spots_list").find('a.spot-details-link').hide();
    $("#spots_list").find("#" + id).find('a.spot-details-link').toggle();
    return $("#spots_list").scrollTop($("#spots_list").scrollTop() + $("#spots_list").find("#" + id).position().top);
  };

  loadMarkers = function(lat, lng) {
    var jqxhr, url, _ref, _ref1;
    if (lat === void 0 || lng === void 0 || lat === null || lng === null) {
      _ref = window.getIPbasedLocation(), lat = _ref[0], lng = _ref[1];
      _ref1 = [Number(lat), Number(lng)], lat = _ref1[0], lng = _ref1[1];
    }
    setCurrenMapCenter(lat, lng);
    window.allSpotsDict = {};
    window.allSpotsArray = [];
    $('#map_canvas').gmap('clear', 'markers');
    url = BASE_HOST + ("/api/nearby/" + (lat.toFixed(5)) + "/" + (lng.toFixed(5)) + "/" + (getDesiredRadius()));
    return jqxhr = $.getJSON(url, function(data) {
      var k, spot, _i, _len, _ref2, _ref3;
      $.each(data, function(i, spot) {
        var SpotIcon, SpotMarker, icony_allowed;
        if (spot.is_enabled !== null) {
          icony_allowed = {
            "true": ICON_URL + "marker-ok.png",
            "false": ICON_URL + "marker-bad.png"
          };
          SpotIcon = {
            url: icony_allowed[spot.is_enabled],
            size: null,
            origin: new google.maps.Point(0, 0),
            anchor: new google.maps.Point(10, 0),
            scaledSize: new google.maps.Size(30 / zoomBasedIconScaleRatio(), 30 / zoomBasedIconScaleRatio())
          };
          SpotMarker = new google.maps.Marker({
            position: new google.maps.LatLng(spot.location.latitude, spot.location.longitude),
            bounds: false,
            id: spot.id,
            is_enabled: [spot.is_enabled],
            spot_type: [spot_type_lookup[spot.spot_type]],
            icon: SpotIcon
          });
          window.allSpotsArray.push(spot);
          return window.allSpotsDict[spot.id] = {
            spot: spot,
            marker: SpotMarker
          };
        }
      });
      $("#map_canvas, #map_filters_button").animate({
        "opacity": "1.0"
      }, "slow");
      $("#spots_list").empty();
      _ref2 = window.allSpotsArray;
      for (_i = 0, _len = _ref2.length; _i < _len; _i++) {
        spot = _ref2[_i];
        $("#spots_list").append(renderSpotsTableViewCell(spot));
      }
      _ref3 = window.allSpotsDict;
      for (k in _ref3) {
        spot = _ref3[k];
        $("#map_canvas").gmap("addMarker", spot.marker).click(function() {
          var userReadOnly;
          $("#map_canvas").gmap("get", "map").panTo(this.getPosition());
          $("#map_canvas").gmap("openInfoWindow", {
            position: this.getPosition(),
            content: renderInfoWindow(allSpotsDict[this.id].spot, userReadOnly = !window.isAuthenticated)
          });
          return activateSpotTableViewCellFor(this.id);
        });
      }
      return filterSpots();
    });
  };

  $(function() {
    var spinner, target;
    target = document.getElementById("map_container");
    spinner = new Spinner(opts).spin(target);
    checkCookies();
    $('body').on('click', function(e) {
      if ($(e.target).parents("#map_filters").length === 0 && e.target.id !== "map_filters_button") {
        return $('#map_filters_button').popover('hide');
      }
    });
    $("#map_filters_button").popover({
      trigger: "click",
      placement: "right",
      html: true,
      title: "Setup your filters:",
      content: "<div id='map_filters' class='no_copy'>\n\n<label class='is_enabled' title='enabled ;-)'>\n<input class='map_filter' type='checkbox' name='is_enabled' hidden></label>\n\n<label class='is_not_enabled' title='NOT enabled :-('>\n<input class='map_filter' type='checkbox' name='is_not_enabled' hidden></label><br><br>\n\n<label class='fa fa-coffee fa-2x mar-r-5' title='Caffee'>\n<input class='map_filter' type='checkbox' name='caffe' hidden></label>\n\n<label class='fa fa-cutlery fa-2x mar-r-5' title='Restaurant'>\n<input class='map_filter' type='checkbox' name='restaurant' hidden></label>\n\n\n<label class='fa fa-bed fa-2x mar-r-5' title='Hotel'>\n<input class='map_filter' type='checkbox' name='hotel' hidden></label>\n\n<label class='fa fa-shopping-cart fa-2x mar-r-5' title='Shop no food'>\n<input class='map_filter' type='checkbox' name='shop - no food' hidden></label>\n\n<label class='fa fa-cart-plus fa-2x mar-r-5' title='Shop with food'>\n<input class='map_filter' type='checkbox' name='shop - with food' hidden></label></div>"
    });
    $(document).on('click', '#back_to_list', function(e) {
      $("#spot_detail").remove();
      switchColumsClasses('#right_container', '#left_container');
      $("#map_filters_button").show();
      $("#spots_list").show();
      $("#map_canvas").gmap("option", "zoom", 14);
      return $('#map_canvas').gmap('refresh');
    });
    $(document).on('click', '#map_filters_button', function(e) {
      return $("#map_filters input.map_filter").each(function() {
        var theCookie;
        theCookie = $.cookie($(this).attr('name'));
        if (theCookie) {
          if (theCookie === "true") {
            $(this).prop('checked', theCookie);
          }
        } else {
          $(this).prop('checked', true);
        }
        return $(this).parent().css('opacity', $(this).prop('checked') === false ? '0.2' : '1');
      });
    });
    $(document).on("change", "#map_filters input.map_filter", function(e) {
      $(this).parent().css('opacity', $(this).prop('checked') === false ? '0.2' : '1');
      $.cookie($(this).attr('name'), $(this).prop('checked'), {
        path: '/map',
        expires: 1
      });
      checkCookies();
      return filterSpots();
    });
    $("#map_canvas").gmap({
      'scrollwheel': false
    }).bind("init", function(evt, map) {
      var options;
      options = {
        timeout: 5000,
        maximumAge: 600000,
        enableHighAccuracy: true
      };
      return $("#map_canvas").gmap("getCurrentPosition", function(position, status, options) {
        var clientPosition;
        if (status === "OK") {
          clientPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        }
        if (clientPosition) {
          loadMarkers(clientPosition.lat(), clientPosition.lng());
        } else {
          loadMarkers(null, null);
        }
        $("#map_canvas").gmap("addMarker", {
          position: new google.maps.LatLng(currentMapCenter.latitude, currentMapCenter.longitude),
          bounds: true,
          is_enabled: ['current_location'],
          spot_type: ['current_location']
        });
        $("#map_canvas").gmap("option", "zoom", 14);
        return spinner.stop();
      });
    });
    $("#map_canvas").on('click', function(e) {
      var clientPosition, newPosition, userZoomLevel;
      newPosition = $('#map_canvas').gmap('get', 'map').getCenter();
      userZoomLevel = $('#map_canvas').gmap('get', 'map').getZoom();
      if (checkIfNewSpotsShouldBeLoaded(newPosition.lat(), newPosition.lng(), userZoomLevel)) {
        setCurrenMapCenter(newPosition.lat(), newPosition.lng());
        currentZoomLevel = $('#map_canvas').gmap('get', 'map').getZoom();
        desiredRadius = Math.floor(currentZoomLevel.getRatioForZoom() / 10 / 2);
        loadMarkers(newPosition.lat(), newPosition.lng());
        return clientPosition = new google.maps.LatLng(currentMapCenter.latitude, currentMapCenter.longitude);
      }
    });
    return $("#spots_list").on("click", "span.list-group-item:not(#memo_empty)", function(evt) {
      var userReadOnly;
      activateSpotTableViewCellFor(this.id);
      $("#map_canvas").gmap("openInfoWindow", {
        position: window.allSpotsDict[this.id].marker.getPosition(),
        content: renderInfoWindow(allSpotsDict[this.id].spot, userReadOnly = !window.isAuthenticated)
      });
      return $("#map_canvas").gmap("get", "map").panTo(window.allSpotsDict[this.id].marker.getPosition());
    });
  });

}).call(this);

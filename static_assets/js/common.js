// Generated by CoffeeScript 1.9.0
(function() {
  var csrfSafeMethod, getCookie, showError, showPosition;

  window.isAuthenticated = eval(DJANGO_USER);

  getCookie = function(name) {
    return $.cookie(name);
  };

  csrfSafeMethod = function(method) {
    return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
  };

  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
      }
    }
  });

  window.getIPbasedLocation = function() {
    var loc;
    console.log("exec IP based geolocation estimation");
    loc = null;
    $.ajax({
      type: 'GET',
      dataType: 'json',
      url: 'http://ipinfo.io/json',
      success: function(result) {
        return loc = result.loc;
      },
      async: false
    });
    return loc;
  };

  window.getGeoLocation = function() {
    if (localStorage.getItem("currentMapCenter")) {
      return JSON.parse(localStorage.getItem("currentMapCenter"));
    } else if (navigator.geolocation) {
      console.log("fetching geo");
      return navigator.geolocation.getCurrentPosition(showPosition, showError);
    }
  };

  window.getCurrentPosition = function() {
    if (localStorage.getItem("currentMapCenter")) {
      return JSON.parse(localStorage.getItem("currentMapCenter"));
    } else {
      return null;
    }
  };

  showPosition = function(position) {
    var currentMapCenter;
    position.coords;
    currentMapCenter = {
      'lat': position.coords.latitude,
      'lng': position.coords.longitude
    };
    localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter));
    return JSON.parse(localStorage.getItem("currentMapCenter"));
  };

  showError = function(error) {
    var currentMapCenter, lat, lng, _ref;
    switch (error.code) {
      case error.PERMISSION_DENIED:
        console.log('User denied the request for Geolocation.');
        break;
      case error.POSITION_UNAVAILABLE:
        console.log('Location information is unavailable.');
        break;
      case error.TIMEOUT:
        console.log('The request to get user location timed out.');
        break;
      case error.UNKNOWN_ERROR:
        console.log('An unknown error occurred.');
    }
    if (error) {
      _ref = getIPbasedLocation().split(','), lat = _ref[0], lng = _ref[1];
      alert('Geolocation is not supported by this browser. We aproximate your locaiton by IP');
      currentMapCenter = {
        'lat': Number(lat),
        'lng': Number(lng)
      };
      localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter));
      return JSON.parse(localStorage.getItem("currentMapCenter"));
    }
  };

  $(function() {
    var check_it;
    if ($("#mobile-menu:hidden").length === 0) {
      $('#smart-menu').show();
    }
    $(window).on('resize', function(e) {
      if ($("#mobile-menu:hidden").length === 0) {
        return $('#smart-menu').show();
      } else {
        return $('#smart-menu').hide();
      }
    });
    $(document).on('click', '#mobile-menu, .show-menu', function(e) {
      e.preventDefault();
      return $('.initialy-invisible').toggle(900);
    });
    $(document).on('click', '#search-icon', function(e) {
      e.preventDefault();
      return $('#search-row').toggle();
    });
    $('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
      console.log($(e.target).attr('href'));
      return console.log(e.relatedTarget);
    });
    $('span.rating').raty({
      scoreName: 'friendly_rate',
      score: function() {
        return $(this).attr('data-score');
      },
      readOnly: function() {
        return !window.isAuthenticated;
      }
    });
    $('span.rating input').attr('type', 'number').attr('required', true);
    $(document).on('click', 'div.heart', function(e) {
      var deleteFavUrl, heart;
      heart = $(this);
      deleteFavUrl = $(this).data('url') + $(this).data('fav-pk') + '/';
      return $.ajax({
        url: deleteFavUrl,
        type: 'DELETE',
        success: function(result) {
          if (window.location.pathname.indexOf('favourites') >= 0) {
            return $(heart).parents('div.thumbnail').remove();
          } else {
            return $(heart).removeClass('heart').addClass('no-heart');
          }
        }
      });
    });
    $(document).on('click', 'div.no-heart:not(.disabled)', function(e) {
      var heart, url;
      heart = $(this);
      url = $(this).data('url');
      return $.ajax({
        url: url,
        data: {
          'spot_pk': $(this).data('spot-pk')
        },
        type: 'POST',
        success: function(result) {
          $(heart).data('fav-pk', result.pk);
          return $(heart).removeClass('no-heart').addClass('heart');
        }
      });
    });
    $(document).on('click', 'div.no-heart.disabled', function(e) {
      return alert('Login required to add spots to favourites!');
    });
    $(document).on('click', 'span.rating.via_modal', function(e) {
      var clickedRate, clickedSpot, rater;
      rater = $(this);
      clickedSpot = rater.attr('id');
      clickedRate = rater.find('input[name="friendly_rate"]').val();
      if (rater.find('input[name="friendly_rate"]').is('[readonly]') === false) {
        $('#rating-modal').find('input[name=spot_pk]').val(clickedSpot);
        $('#rating-modal').find('#modal_rating').raty({
          score: clickedRate,
          scoreName: 'friendly_rate',
          size: 24,
          starOff: STATIC_URL + 'star-off-big.png',
          starHalf: STATIC_URL + 'star-half-big.png',
          starOn: STATIC_URL + 'star-on-big.png'
        });
        $('#rating-modal').find('input[name=friendly_rate]').val(clickedRate);
        return $('#rating-modal').modal('show');
      } else {
        return alert('Login required to rate spots!');
      }
    });
    check_it = function(radio_allowance) {
      if ($(radio_allowance).prop('checked') === false) {
        return $(radio_allowance).parent().css('opacity', '0.2');
      } else {
        return $(radio_allowance).parent().css('opacity', '1');
      }
    };
    $('#rating-modal').on('click', '#allowance', function(e) {
      return $(this).find('input.allowance').each(function(index, element) {
        return check_it(this);
      });
    });
    $('#rating-modal').on('submit', '#rating-form', function(e) {
      var data;
      e.preventDefault();
      data = JSON.stringify($('#rating-form').serializeJSON({
        parseBooleans: true,
        parseNulls: true,
        parseNumbers: true
      }));
      return $.ajax({
        url: '/api/ratings/',
        data: data,
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        type: 'POST',
        success: function(result) {
          $('#rating-modal').modal('hide');
          return window.location.reload();
        }
      });
    });
    $.widget("custom.autocomplete", $.ui.autocomplete, {
      _create: function() {
        this._super();
        return this.widget().menu("option", "items", "> :not(.ui-autocomplete-category)");
      },
      _renderMenu: function(ul, items) {
        var currentCategory;
        currentCategory = '';
        return $.each(items, (function(_this) {
          return function(index, item) {
            var li;
            if (item.category !== currentCategory) {
              currentCategory = item.category;
              ul.append("<li class='ui-autocomplete-category'>" + currentCategory + "</li>");
            }
            li = _this._renderItemData(ul, item);
            if (item.thumb) {
              if (item.category) {
                return li.find("a").attr('href', item.url).html("<img src=" + item.thumb + " class='search_thumb'>" + item.name);
              }
            } else {
              if (item.category) {
                return li.find("a").attr('href', item.url).html("<div class='search_thumb_placeholder'></div>" + item.name);
              }
            }
          };
        })(this));
      }
    });
    return $("input#main_menu_search").autocomplete({
      minLength: 1,
      delay: 300,
      autoFocus: false,
      source: function(request, response) {
        return $.ajax({
          data: {
            q: request.term
          },
          url: "/ajax_search/",
          dataType: "json",
          success: function(data) {
            return response(data);
          }
        });
      },
      focus: function(e, ui) {
        e.preventDefault();
        return $(this).val(ui.item.category + ": " + ui.item.name);
      },
      select: function(e, ui) {
        var uri;
        uri = ui.item.url;
        return window.location = uri;
      },
      close: function(e, ui) {
        return $(e.target).val('');
      }
    });
  });

}).call(this);

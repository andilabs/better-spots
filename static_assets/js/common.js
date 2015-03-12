// Generated by CoffeeScript 1.9.0
(function() {
  var csrfSafeMethod, getCookie;

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

  $(function() {
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
    $(document).on('click', 'span.heart', function(e) {
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
    $(document).on('click', 'span.no-heart:not(.disabled)', function(e) {
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
    $(document).on('click', 'span.no-heart.disabled', function(e) {
      return alert('Login required to add spots to favourites!');
    });
    $(document).on('click', 'span.rating.via_modal', function(e) {
      var clickedRate, clickedSpot, rater;
      rater = $(this);
      clickedSpot = rater.attr('id');
      console.log(clickedSpot);
      clickedRate = rater.find('input[name="friendly_rate"]').val();
      if (rater.find('input[name="score"]').is('[readonly]') === false) {
        $('#rating-modal').find('input[name=spot_pk]').val(clickedSpot);
        $('#rating-modal').find('#modal_rating').raty({
          score: clickedRate,
          scoreName: 'friendly_rate'
        });
        $('#rating-modal').find('input[name=friendly_rate]').val(clickedRate);
        return $('#rating-modal').modal('show');
      } else {
        return alert('Login required to rate spots!');
      }
    });
    window.check_it = function(foo) {
      if ($(foo).prop('checked') === false) {
        return $(foo).parent().css('opacity', '0.2');
      } else {
        return $(foo).parent().css('opacity', '1');
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
      console.log(data);
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

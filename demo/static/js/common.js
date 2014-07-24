// Generated by CoffeeScript 1.7.1
(function() {
  $(function() {
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
            console.log(item.url, item.name);
            if (item.category) {
              return li.find("a").attr('href', item.url).html("" + item.name);
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
            console.log(data);
            return response(data);
          }
        });
      },
      focus: function(e, ui) {
        e.preventDefault();
        return $(this).val("" + ui.item.category + ": " + ui.item.name);
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

// Generated by CoffeeScript 1.9.0
(function() {
  $(function() {
    $(".venue_photo").fadeTo(0, 0.5);
    return $(".venue_photo").hover(function(e) {
      return $(e.target).stop().fadeTo(300, e.type === 'mouseenter' ? 1 : 0.5);
    });
  });

}).call(this);

$ ->

    $(".venue_photo").fadeTo(0, 0.5) # initial opacity

    $(".venue_photo").hover (e) ->
       $(e.target).stop().fadeTo 300, if e.type == 'mouseenter' then 1 else 0.5

$ ->
    if window.chrome
        $('.banner li').css 'background-size', '100% 100%'

    $('.banner').unslider
        speed: 1500
        arrows: false
        fluid: true
        dots: true
    #  Find any element starting with a # in the URL
    #  And listen to any click events it fires
    $('a[href^="#"]').click ->
        #  Find the target element
        target = $($(this).attr('href'))
        #  And get its position
        pos = target.offset()
        # fallback to scrolling to top || {left: 0, top: 0};
        #  jQuery will return false if there's no element
        #  and your code will throw errors if it tries to do .offset().left;
        if pos
        #  Scroll the page
            $('html, body').animate {
              scrollTop: pos.top
              scrollLeft: pos.left
            }, 1500
        #  Don't let them visit the url, we'll scroll you there
        false

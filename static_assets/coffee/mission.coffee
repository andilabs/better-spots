$ ->
    if window.chrome
        $('.banner li').css 'background-size', '100% 100%'

    $('.banner').unslider
        speed: 1500
        arrows: false
        fluid: true
        dots: true


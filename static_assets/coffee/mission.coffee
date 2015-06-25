
$ ->

    if window.chrome
        $('.banner li').css 'background-size', '100% 100%'

    $('.banner').unslider
        speed: 1500
        arrows: false
        fluid: true
        dots: true

    $('a.show-menu').on 'click', (e) ->
        e.preventDefault()
        $('.initialy-invisible').show(900)

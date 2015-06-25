window.isAuthenticated = eval(DJANGO_USER)

getCookie = (name) ->
    $.cookie(name)

csrfSafeMethod = (method) ->
    # these HTTP methods do not require CSRF protection
    /^(GET|HEAD|OPTIONS|TRACE)$/.test method

$.ajaxSetup beforeSend: (xhr, settings) ->
    if !csrfSafeMethod(settings.type) and !@crossDomain
        xhr.setRequestHeader 'X-CSRFToken', getCookie('csrftoken')
    return

window.getIPbasedLocation = () ->
    console.log "exec IP based geolocation estimation"
    loc = null
    $.ajax
        type: 'GET'
        dataType: 'json'
        url: 'http://ipinfo.io/json'
        success: (result) ->
            loc = result.loc
        async: false
    return loc

window.getGeoLocation = () ->
    if localStorage.getItem("currentMapCenter")
        return JSON.parse(localStorage.getItem("currentMapCenter"))
    else if navigator.geolocation
        console.log "fetching geo"
        return navigator.geolocation.getCurrentPosition showPosition, showError

window.getCurrentPosition = () ->
    if localStorage.getItem("currentMapCenter")
        return JSON.parse(localStorage.getItem("currentMapCenter"))
    else
        return null

showPosition = (position) ->
    position.coords
    currentMapCenter = {'lat':position.coords.latitude, 'lng': position.coords.longitude}
    localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter))
    return JSON.parse(localStorage.getItem("currentMapCenter"))


showError = (error) ->
    switch error.code
        when error.PERMISSION_DENIED
            console.log 'User denied the request for Geolocation.'
        when error.POSITION_UNAVAILABLE
            console.log 'Location information is unavailable.'
        when error.TIMEOUT
            console.log 'The request to get user location timed out.'
        when error.UNKNOWN_ERROR
            console.log 'An unknown error occurred.'
    if error
        [lat, lng] = getIPbasedLocation().split(',')
        alert 'Geolocation is not supported by this browser. We aproximate your locaiton by IP'
        currentMapCenter = {'lat':Number(lat), 'lng': Number(lng)}
        localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter))
        return JSON.parse(localStorage.getItem("currentMapCenter"))

$ ->
    if $("#mobile-menu:hidden").length == 0
        $('#smart-menu').show()

    $(window).on 'resize', (e) ->
        if $("#mobile-menu:hidden").length == 0
            $('#smart-menu').show()
        else
            $('#smart-menu').hide()

    $(document).on 'click', '#mobile-menu, .show-menu', (e) ->
        console.log "wtf?"
        e.preventDefault()
        $('.initialy-invisible').toggle(900)

    $('a[data-toggle="tab"]').on 'shown.bs.tab',  (e) ->
      console.log $(e.target).attr('href')# newly activated tab
      console.log e.relatedTarget# previous active tab


    $('span.rating').raty
        scoreName: 'friendly_rate'
        score: ->
            $(this).attr 'data-score'
        readOnly: ->
            !window.isAuthenticated


    $('span.rating input').attr('type', 'number').attr 'required', true


    $(document).on 'click', 'div.heart', (e) ->
        heart = $(this)
        deleteFavUrl = $(this).data('url') + $(this).data('fav-pk') + '/'
        $.ajax
            url: deleteFavUrl
            type: 'DELETE'
            success: (result) ->
                if window.location.pathname.indexOf('favourites') >= 0
                    $(heart).parents('div.thumbnail').remove()
                else
                    $(heart).removeClass('heart').addClass 'no-heart'


    $(document).on 'click', 'div.no-heart:not(.disabled)', (e) ->
        heart = $(this)
        url = $(this).data('url')
        $.ajax
            url: url
            data: 'spot_pk': $(this).data('spot-pk')
            type: 'POST'
            success: (result) ->
                $(heart).data 'fav-pk', result.pk
                $(heart).removeClass('no-heart').addClass 'heart'


    $(document).on 'click', 'div.no-heart.disabled', (e) ->
        alert 'Login required to add spots to favourites!'


    $(document).on 'click', 'span.rating.via_modal', (e) ->
        rater = $(this)
        clickedSpot = rater.attr('id')
        clickedRate = rater.find('input[name="friendly_rate"]').val()
        if rater.find('input[name="friendly_rate"]').is('[readonly]') == false
            $('#rating-modal').find('input[name=spot_pk]').val(clickedSpot)
            $('#rating-modal').find('#modal_rating').raty({
                score: clickedRate,
                scoreName: 'friendly_rate',
                size: 24,
                starOff: STATIC_URL+'star-off-big.png',
                starHalf: STATIC_URL+'star-half-big.png',
                starOn: STATIC_URL+'star-on-big.png'})
            $('#rating-modal').find('input[name=friendly_rate]').val(clickedRate)
            $('#rating-modal').modal('show')
        else
            alert 'Login required to rate spots!'

    check_it = (radio_allowance) ->
        if $(radio_allowance).prop('checked') == false
            $(radio_allowance).parent().css 'opacity', '0.2'
        else
            $(radio_allowance).parent().css 'opacity', '1'


    $('#rating-modal').on 'click', '#allowance', (e) ->
        $(this).find('input.allowance').each (index, element) ->
            check_it this



    $('#rating-modal').on 'submit', '#rating-form', (e) ->
        e.preventDefault()
        data = JSON.stringify($('#rating-form').serializeJSON(
            parseBooleans: true
            parseNulls: true
            parseNumbers: true))

        $.ajax
            url: '/api/ratings/'
            data: data
            contentType: "application/json; charset=utf-8"
            dataType: "json"
            type: 'POST'
            success: (result) ->
                $('#rating-modal').modal('hide')
                window.location.reload()

    $.widget "custom.autocomplete", $.ui.autocomplete,
        _create: () ->
            @_super()
            @widget().menu "option", "items", "> :not(.ui-autocomplete-category)"


        _renderMenu: (ul, items) ->
            currentCategory = ''
            $.each items, (index, item) =>
                if item.category != currentCategory
                    currentCategory = item.category
                    ul.append "<li class='ui-autocomplete-category'>#{currentCategory}</li>"
                li = @_renderItemData(ul, item)
                if item.thumb
                    li.find("a").attr('href',item.url).html("<img src=#{item.thumb} class='search_thumb'>#{item.name}") if item.category
                else
                    li.find("a").attr('href',item.url).html("<div class='search_thumb_placeholder'></div>#{item.name}") if item.category



    $("input#main_menu_search").autocomplete
        minLength: 1
        delay: 300
        autoFocus: false
        source: (request, response) ->
            $.ajax
                data: {q: request.term}
                url: "/ajax_search/"
                dataType: "json"

                success: (data) ->
                    response data

        focus: (e, ui) ->
            e.preventDefault()
            $(@).val("#{ui.item.category}: #{ui.item.name}")


        select: (e, ui) ->
            uri = ui.item.url
            window.location = uri

        close: (e, ui) ->
            $(e.target).val('')

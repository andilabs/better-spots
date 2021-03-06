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
        url: 'https://freegeoip.net/json/'
        success: (result) ->
            loc = [result.latitude, result.longitude]
            return loc
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
        [lat, lng] = getIPbasedLocation()
        alert 'Geolocation is not supported by this browser. We aproximate your locaiton by IP'
        currentMapCenter = {'lat':Number(lat), 'lng': Number(lng)}
        localStorage.setItem('currentMapCenter', JSON.stringify(currentMapCenter))
        return JSON.parse(localStorage.getItem("currentMapCenter"))

confirm_login_redirect = (msg) ->
    confirmation = confirm("#{msg} Would you like to login now?")
    if confirmation
        location.href = LOGIN_URL

$ ->
    if $("#mobile-menu:hidden").length == 0
        $('#smart-menu').show()

    $(document).on 'keyup', 'input#smart_menu_search', (e) ->
        console.log $(e.target).val().length
        if $(e.target).val().length != 0
            $("#search-remover").removeClass('glyphicon glyphicon-search')
            $("#search-remover").addClass('glyphicon glyphicon-remove')
        else
            $("#search-remover").removeClass('glyphicon glyphicon-remove')
            $("#search-remover").addClass('glyphicon glyphicon-search')

    $(document).on 'click', 'a#search-remove-helper i.glyphicon-remove', (e) ->
        e.preventDefault()
        $('input#smart_menu_search').val('')
        $("#search-remover").removeClass('glyphicon glyphicon-remove')
        $("#search-remover").addClass('glyphicon glyphicon-search')
        $('#smart_menu_search').focus()

    $(window).on 'resize', (e) ->
        if $("#mobile-menu:hidden").length == 0
            $('#smart-menu').show()
        else
            if window.location.pathname != '/'
                $('#smart-menu').hide()

    $(document).on 'click', '#mobile-menu, .show-menu', (e) ->
        e.preventDefault()
        $('.initialy-invisible').toggle(900)

    $(document).on 'click', '#search-icon', (e) ->
        e.preventDefault()
        $('#search-row').toggle()
        $('#smart_menu_search').focus()

    $(document).on 'click', '#go-top', (e) ->
        e.preventDefault()
        $('#smart-menu').show()
        window.scrollTo(0,0)
        $('.initialy-invisible').show(900)


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

    # REMOVE FROM FAVOURITES
    $(document).on 'click', 'div.heart', (e) ->
        heart = $(this)
        $.ajax
            url: $(this).data('spot-detail-url')
            type: 'DELETE'
            success: (result) ->
                if window.location.pathname.indexOf('favourites') >= 0
                    $(heart).parents('div.thumbnail').remove()
                else
                    $(heart).removeClass('heart').addClass 'no-heart'

    # ADD TO FAVOURITES
    $(document).on 'click', 'div.no-heart:not(.disabled)', (e) ->
        heart = $(this)
        url = $(this).data('spot-list-url')
        $.ajax
            url: url
            data: 'spot': $(this).data('spot-pk')
            type: 'POST'
            success: (result) ->
                $(heart).data 'spot-detail-url', result.url
                $(heart).removeClass('no-heart').addClass 'heart'




    $(document).on 'click', 'div.no-heart.disabled', (e) ->
        msg = 'Login required to add spots to favourites!'
        return confirm_login_redirect(msg)


    $(document).on 'click', 'span.rating.via_modal', (e) ->
        rater = $(this)
        clickedSpot = rater.data('spot-pk')
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
            msg = 'Login required to rate spots!'
            return confirm_login_redirect(msg)

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

        spot_pk = JSON.parse(data).spot_pk
        $.ajax
            url: "/api/spots/#{spot_pk}/rates/"
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
                if item.thumbnail_venue_photo
                    li.find("a").attr('href',item.www_url).html(
                        "<img src=#{item.thumbnail_venue_photo} class='search_thumb'>
                        <span class='search-spot-name'>#{item.name}</span>
                        <span class='search-spot-address'>#{item.address_city}, #{item.address_street}  #{item.address_number}</span>") if item.category
                else
                    li.find("a").attr('href',item.www_url).html("<div class='search_thumb_placeholder'></div><span class='search-spot-name'>#{item.name}</span>
                        <span class='search-spot-address'>#{item.address_city}, #{item.address_street}  #{item.address_number}</span>") if item.category



    $("input#main_menu_search, input#smart_menu_search").autocomplete
        minLength: 1
        delay: 300
        autoFocus: false
        source: (request, response) ->
            $.ajax
                data: {search_query: request.term}
                url: FTS_SEARCH_API_ENDPOINT
                dataType: "json"

                success: (data) ->
                    response data.results

        focus: (e, ui) ->
            e.preventDefault()
            $(@).val("#{ui.item.category}: #{ui.item.name}")


        select: (e, ui) ->
            uri = ui.item.www_url
            window.location = uri

        close: (e, ui) ->
            $(e.target).val('')

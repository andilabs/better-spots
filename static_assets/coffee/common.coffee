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

$ ->

    $('span.rating').raty
        scoreName: 'friendly_rate'
        score: ->
            $(this).attr 'data-score'
        readOnly: ->
            !window.isAuthenticated


    $('span.rating input').attr('type', 'number').attr 'required', true


    $(document).on 'click', 'span.heart', (e) ->
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


    $(document).on 'click', 'span.no-heart:not(.disabled)', (e) ->
        heart = $(this)
        url = $(this).data('url')
        $.ajax
            url: url
            data: 'spot_pk': $(this).data('spot-pk')
            type: 'POST'
            success: (result) ->
                $(heart).data 'fav-pk', result.pk
                $(heart).removeClass('no-heart').addClass 'heart'


    $(document).on 'click', 'span.no-heart.disabled', (e) ->
        alert 'Login required to add spots to favourites!'


    $(document).on 'click', 'span.rating.via_modal', (e) ->
        rater = $(this)
        clickedSpot = rater.attr('id')
        clickedRate = rater.find('input[name="friendly_rate"]').val()
        console.log "spot:", clickedSpot
        console.log "rate:", clickedRate
        if rater.find('input[name="friendly_rate"]').is('[readonly]') == false
            $('#rating-modal').find('input[name=spot_pk]').val(clickedSpot)
            $('#rating-modal').find('#modal_rating').raty({score: clickedRate, scoreName: 'friendly_rate'})
            $('#rating-modal').find('input[name=friendly_rate]').val(clickedRate)
            $('#rating-modal').modal('show')
        else
            alert 'Login required to rate spots!'

    window.check_it = (foo) ->
        if $(foo).prop('checked') == false
            $(foo).parent().css 'opacity', '0.2'
        else
            $(foo).parent().css 'opacity', '1'


    $('#rating-modal').on 'click', '#allowance', (e) ->
        $(this).find('input.allowance').each (index, element) ->
            check_it this



    $('#rating-modal').on 'submit', '#rating-form', (e) ->
        e.preventDefault()
        data = JSON.stringify($('#rating-form').serializeJSON(
            parseBooleans: true
            parseNulls: true
            parseNumbers: true))
        console.log data
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

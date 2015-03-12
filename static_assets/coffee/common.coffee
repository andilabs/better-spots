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


    $(document).on 'click', 'span.rating', (e) ->
        rater = $(this)
        if rater.find('input[name="score"]').is('[readonly]') == false
            $.ajax
                url: '/api/ratings/'
                data:
                    'spot_pk': rater.attr('id')
                    'friendly_rate': rater.find('input[name="friendly_rate"]').val()
                type: 'POST'
                success: (result) ->
                    selector = 'span#' + $(rater).attr('id')
                    $(selector).raty score: result.new_score
        else
            alert 'Login required to rate spots!'

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
                # selector = 'span#' + $(rater).attr('id')
                # $(selector).raty score: result.new_score
                $('#rating-modal').modal('hide')

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
                console.log item.url, item.name
                li.find("a").attr('href',item.url).html("#{item.name}") if item.category


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
                    console.log data
                    response data

        focus: (e, ui) ->
            e.preventDefault()
            $(@).val("#{ui.item.category}: #{ui.item.name}")


        select: (e, ui) ->
            uri = ui.item.url
            window.location = uri

        close: (e, ui) ->
            $(e.target).val('')

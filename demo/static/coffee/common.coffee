$ ->
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

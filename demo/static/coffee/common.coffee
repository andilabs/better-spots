$ ->

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

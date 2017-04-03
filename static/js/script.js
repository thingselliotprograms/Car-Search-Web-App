$(document).ready(function () {
    $('.select-maker').hide(),
    $('#select-by-maker').click(function () {
        $('.select-maker').show();
    }),
    $('#sort-by-quality').click(function () {
        $('.select-maker').hide();
    }),
    $(function () {
        $('.carmakers').bind('click', function () {
            $('#maseratimodels').text()
            $.getJSON('/modelssamepage', {
                maker: $(this).text()
            }, function (data) {
                $('#maseratimodels').empty()
                console.log(data);
                $.each(data, function (key, value) {
                    $('#maseratimodels').append("<li class='list-group-item'><h3>" + value + "</h3></li>")
                });
            })
            return false;
        });
    })
    });
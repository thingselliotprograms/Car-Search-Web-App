$(document).ready(function () {
    $('.select-maker').hide(),
    $('#maker-header').hide(),
    $('#quality-activity').hide()
    $('.qual2').hide()
    $('.qual3').hide()
    $('#select-by-maker').click(function () {
        $('.select-maker').show();
        //$('#maker-models-container').show();
        $('#quality-activity').hide()
    }),
    $('#sort-by-quality').click(function () {
        $('.select-maker').hide();
        $('#quality-activity').show()
    }),
    $(function () {
        $('.carmakers').bind('click', function () {
            $('#maker-models').text();
            $('#maker-header-text').empty();
            $('#model-styles-list').empty();
            $('#model-styles-header-text').empty()
            $('#back-to-models').empty();
            $('#maker-header').prepend('<h1 id="maker-header-text">' + $(this).text() + ' Models</h1>')
            $('#maker-models-container').show();
            $('#maker-header').show();
            $.getJSON('/modelssamepage', {
                maker: $(this).text()
            }, function (data) {
                $('#maker-models').empty()
                console.log(data);
                $.each(data, function (key, value) {
                    $('#maker-models').append("<li class='list-group-item'><a role='menuitem' class='model-list-item' href=#><h3>" + value + "</h3></a></li>")
                });
            })
            return false;
        });
    }),
    $(function () {
        $('.list-group').on('click', 'a', function () {
            makerstr = $('#maker-header-text').text()
            makerstrslice = makerstr.slice(0, -7)
            modelstr = $(this).text();
            $('#model-styles-header-text').empty()
            $('#model-styles-list').empty()
            $('#maker-models-container').hide();
            $('#model-styles').show();
            $('#model-styles-header').prepend('<h1 id="model-styles-header-text">' + makerstrslice + ' ' + modelstr + ' Styles</h1><h4><a href=# id="back-to-models">Back to '+makerstrslice+' Models</a></h4>')
            $.getJSON('/modelstyles', {
                maker: makerstrslice,
                model: modelstr
            }, function (data) {
                console.log(data);
                $.each(data, function (key, value) {
                    console.log(data[key])
                    x = data[key]
                    $('#model-styles-list').append("<li class='list-group-item'><h3>"
                        + x['model_year'] + " " + x['submodel_name'] + "</h3>"
                        + "<p>" + x['detailed_name'] + "</p>" +
                        "<p>$" + x['price'] + "</p>" +
                        "</li>")
                })

            })
        })
    }),
    $(function () {
        $('#model-styles-header').on('click', 'a', function () {
            $('#model-styles').hide()
            $('#maker-models-container').show()
            $('#back-to-models').empty()
        })
    }),
    $(function () {
        $('#sel1').on('click', function () {
            option1 = $('#sel1').val()
            option2 = $('#sel2').val()
            option3 = $('#sel3').val()
            if (option1 !== "None") {
                $('.qual2').show()
                $('.qual3').hide()
            }
            else {
                $('.qual2').hide()
                $('#sel2').val("None")
                $('.qual3').hide()
                $('#sel3').val("None")
            }
        })
    }),
    $(function () {
        $('#sel2').on('click', function () {
            option2 = $('#sel2').val()
            if (option2 !== "None") {
                $('.qual3').show()
            }
            else {
                $('.qual3').hide()
                $('#sel3').val("None")

            }
        })
    }),
    $(function () {
        $('.submit-btn').on('click', function () {
            option1 = $('#sel1').val()
            option2 = $('#sel2').val()
            option3 = $('#sel3').val()
            console.log("Find " + option1, option2, option3)
            if (option1 === "None") {
                alert("No criteria chosen for search!")
            }
            else {
                $('#vehicle-results-list').empty()
                $('#selection-title').empty()
                $('#selection-title').append('Top 25 Results <span style="font-style:italic">('+option1+', '+option2+', '+option3+')</span>')
                optionsary = []
                optionsary.push(option1)
                optionsary.push(option2)
                optionsary.push(option3)
                console.log(optionsary)
                $.getJSON('/orderbyqualities', {
                    quality1: optionsary[0],
                    quality2: optionsary[1],
                    quality3: optionsary[2]
                }, function (data) {
                    console.log(data)
                    $.each(data, function (key, value) {
                        console.log(data[key])
                        x = data[key]
                        $('#vehicle-results-list').append(
                            "<li class='list-group-item'><h3>"
                            + "<span>" + x['model_year'] + " " + x['maker'] + " " + x['submodel_name'] + "</span>" +
                            "<span style='float:right;padding-right:15px'>$" + x['price'] + "</span></h3>"
                            + "<p>" + x['detailed_name'] + "</p>" +
                            "<div class='container-fluid extra-info'><p>Specifications:</p>" +
                            "<p>Performance: "+x['hp']+" Horsepower ------"+ "Torque: "+x['torque']+ " lbf*ft</p>"+
                            "<p>Engine: Type: "+x['engine_type']+" ------ "+ x['cylinders'] + " Cylinders ------ Size: "+ x['engine_size']+" Liters</p>" +
                            "<p>Economy: Highway MPG: " + x['mpg_hw'] + " ------  City MPG: " + x['mpg_city'] + "</p>" +
                            "<p>Transmission: Type: "+x['trans_type']+" ------ Speeds: "+x['trans_num_speeds']+"</p>"+
                            "</div>" +
                            "</li>")
                    })
                })
            }
            
        })
        
    })
    return false;
});
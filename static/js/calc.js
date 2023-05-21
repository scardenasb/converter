$(document).ready(function() {

    // NOTE: Ajax to render dropdowns
    $('#id_unit_type').on('change', function() {
        var type_id = $(this).val();
        if (type_id !== "") {
            $.ajax({
                url: '/ajax_view/',
                method: 'GET',
                data: {
                    type_id: type_id
                },
                success: function(response) {
                    cleanOptions();
                    var data = response.data
                    for (var i = 0; i < data.length; i++) {
                        unit = data[i]
                        $('#id_unit_from, #id_unit_to').append($('<option>', {
                            value: unit.id,
                            text: unit.abbreviation
                        }))
                    }
                    $('#id_unit_from').trigger('change')
                }
            })
        }
    });

    // NOTE: Ajax to render result
    $('#submit-button').on('click', function() {
        var type_id = $('#id_unit_type').val();
        var from_id = $('#id_unit_from').val();
        var to_id = $('#id_unit_to').val();
        var value = $('#id_unit_value').val();
        if (type_id !== "") {
            $.ajax({
                url: '/ajax_result/',
                method: 'GET',
                data: {
                    type_id: type_id,
                    from_id: from_id,
                    to_id: to_id,
                    value: value,
                },
                success: function(response) {
                    console.log(response.data.text)
                    var result = response.data.text
                    $('#result').text(result)

                }

            })
        }
    });
});

function onlyNumberKey(evt) {

    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57) && ASCIICode != 46)
        return false;
    return true;
}

function cleanOptions() {
    var to = $('#id_unit_to')
    var from = $('#id_unit_from')
    var value = $('#id_unit_value')
    var result = $('#result')
    to.empty().append($('<option>', {
        value: '',
        text: '-------'
    }))
    from.empty().append($('<option>', {
        value: '',
        text: '-------'
    }))
    value.val('')
    result.text('')
}

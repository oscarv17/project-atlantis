var ex_categories = []
var in_categories = []
var count_id = 0

$('#add_expense').click(function () { 
    append_row('expenses', ex_categories);
});

$('#add_income').click(function () { 
    append_row('incomes', in_categories);
});

function append_row(action, categories) {
    $('#'+action).each(function () {
       count_id++;
        var tds = '<tr>';
        $.each($('tr:last', this), function () {
            tds += '<td>' + '<input type="text" class="form-control datepicker" placeholder="Fechas">' + '</td>';
            tds += '<td>' + '<input type="number" class="form-control" placeholder="Monto">' + '</td>';
            tds += '<td>' + '<input type="text" class="form-control" placeholder="Descripcion">' + '</td>';
            tds += '<td>' + '<select class="form-control" id="categories'+count_id+'"></select>' + '</td>';
        });
        tds += '</tr>';
        if ($('tbody', this).length > 0) {
            $('tbody', this).append(tds);
        } else {
            $(this).append(tds);
        }
        $('.datepicker').datepicker();
    });
    if(categories.length > 0) {
        populateSelect(categories, count_id);
    } else {
        get_categories(action, count_id);
    }
}

function get_categories(action, count_id) {
    $.ajax({
        url: '/ajax/get/categories/',
        data: { 'action': action },
        dataType: 'json',
        success: function(data) {
            if(action=='expenses') {
                ex_categories =  data.categories;
            } else {
                in_categories = data.categories;
            }
            populateSelect(data.categories, count_id);
        },
    });
}

function populateSelect(categories, count_id) {
    $.each(categories, function (index, value) {
        $('#categories'+count_id).append($('<option/>', { 
            value: value,
            text : value 
        }));
    });   
}
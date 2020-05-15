var ex_categories = []
var in_categories = []
var count_id = 0

$('#add_expense').click(function () { 
    append_row('expenses');
});

$('#add_income').click(function () { 
    append_row('incomes');
});

function append_row(action) {
    $('#'+action).each(function () {
       count_id++;
        var tds = '<tr>';
        $.each($('tr:last', this), function () {
            get_categories(action, count_id, $(this));
            // tds += '<td>' + '<input type="text" class="form-control datepicker" placeholder="Fechas">' + '</td>';
            // tds += '<td>' + '<input type="number" class="form-control" placeholder="Monto">' + '</td>';
            // tds += '<td>' + '<input type="text" class="form-control" placeholder="Descripcion">' + '</td>';
            // tds += '<td>' + '<select class="form-control" id="categories'+count_id+'"></select>' + '</td>';
        });
        tds += '</tr>';
        $('tbody', this).append(tds);
        
    });
    // if(categories.length > 0) {
    //     populateSelect(categories, count_id);
    // } else {
        // get_categories(action, count_id);
    //}
    if(action=='expenses') {
        if (!$('#sendExpense').length) {
            $('#formExpense').append('<button type="submit" class="btn btn-primary move-button" id="sendExpense">Guradar</button>')
        }
    } else {
        if (!$('#sendIncome').length) {
            $('#formIncome').append('<button type="submit" class="btn btn-primary move-button" id="sendIncome">Guradar</button>')
        }
    }
}

function get_categories(action, count_id, obj) {
    $.ajax({
        url: '/manage/movements/',
        data: { 'action': action },
        success: function(data) {
            $(obj).html(data)
            $('.datepicker').datepicker();
            // if(action=='expenses') {
            //     ex_categories =  data.categories;
            // } else {
            //     in_categories = data.categories;
            // }
            // populateSelect(data.categories, count_id);
        },
    });
}

// function populateSelect(categories, count_id) {
//     $.each(categories, function (index, value) {
//         $('#categories'+count_id).append($('<option/>', { 
//             value: value,
//             text : value 
//         }));
//     });   
// }
$('#add_expense').click(function () { 
    append_row('expenses');
});

$('#add_income').click(function () { 
    append_row('incomes');
});

function append_row(action) {
    $('#'+action).each(function () {
        var tds = '<tr class="new-form">';
        $.each($('tr:last', this), function () {
            get_categories(action, $(this));
        });
        tds += '</tr>';
        $('tbody', this).append(tds);
        
    });
    if (!$('#sendExpense').length && action=='expenses') {
        $('#formExpense').append('<button type="submit" class="btn btn-primary move-button" id="'+getId(action)+'">Guradar  <i class="fas fa-save"></i></button>');
    
    } else if (!$('#sendIncome').length && action=='incomes') {
        $('#formIncome').append('<button type="submit" class="btn btn-primary move-button" id="'+getId(action)+'">Guradar  <i class="fas fa-save"></i></button>');
    }
}

function get_categories(action, obj) {
    $.ajax({
        url: '/manage/movements/',
        data: { 'action': action },
        success: function(data) {
            $(obj).html(data);

            $('.datepicker').datepicker();

            $('.delete-row').on('click', function(){
                $(this).parents('tr:first').remove();
                if($('table#'+action+' .new-form').length < 2) {
                    $('#'+getId(action)).remove()
                }
            });
        },
    });
}

function getId(action) {
    if(action=='expenses') {
        return 'sendExpense';
    }
    return 'sendIncome'
}
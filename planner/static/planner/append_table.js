$('#add_expense').click(function() { 
    append_row('expenses');
});

$('#add_income').click(function() { 
    append_row('incomes');
});

$('.fa-edit').click(function() {
    var tr = $(this).parents('tr');;
    var inputs = get_input_texts(tr.children());
    var action = $(this).parents('table').attr('id');

    get_categories(action, $(tr), true, inputs);
   
});

function append_row(action) {
    $('#'+action).each(function () {
        var tds = '<tr class="new-form">';
        $.each($('tr:last', this), function () {
            get_categories(action, $(this), false);
        });
        tds += '</tr>';
        $('tbody', this).append(tds); 
    });
}

function get_categories(action, obj, edit, texts = []) {
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

            appendButton(action);

            if(edit) {
                createEditSection(obj, texts);
            }
               
        },
    });
}

function getId(action) {
    if(action=='expenses') {
        return 'sendExpense';
    }
    return 'sendIncome'
}

function appendButton(action) {
    if (!$('#sendExpense').length && action=='expenses') {
        $('#formExpense').append('<button type="submit" class="btn btn-primary move-button" id="'+getId(action)+'">Guradar  <i class="fas fa-save"></i></button>');
    
    } else if (!$('#sendIncome').length && action=='incomes') {
        $('#formIncome').append('<button type="submit" class="btn btn-primary move-button" id="'+getId(action)+'">Guradar  <i class="fas fa-save"></i></button>');
    }
}

function get_input_texts(tds) {
    var arr = [];
    for (var i = 0; i < tds.length - 1; i++) {
        arr[i] = $(tds[i]).text();
    }
    return arr;
}

function createEditSection(obj, texts) {
    var id = $(obj).attr('id').split('-')[1];
    var inputs = $(obj).find('input');
    var select = $(obj).find('select');

    for (var i = 0; i < inputs.length; i++) {
        if(i==1){
            var amount = parseFloat(texts[i].split('$')[1].replace(',', ''));
            $(inputs[i]).val(amount);
        } else {
            $(inputs[i]).val(texts[i]);
        }
    }

    $(select.children()).filter(function() {
        return $(this).text() == texts[3];
      }).prop('selected', true);

      $(obj).append('<td style="display:none"><input type="hidden" name="edit-id"  value='+id+'/></td>');
}
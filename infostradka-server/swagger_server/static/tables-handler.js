$(document).ready(function() {
    // rows change
    $("#settings-tbl").tableDnD();

    // date-time range picker
    $('input[name="start_stop_time"]').daterangepicker({
        timePicker: true,
        startDate: moment().startOf('hour'),
        endDate: moment().startOf('hour').add(32, 'hour'),
        locale: {
          format: 'DD.MM.Y HH:mm'
        }
    });

    // content-type picker
    $('select[name="content_type"]').change(function(event){
        var url = $(event.target).parent().parent().find('input[name="url"]');
        var file = $(event.target).parent().parent().find('select[name="file_hash"]');

        if(event.target.value == 'file'){
            url.hide();
            file.show();
        } else {
            url.show();
            file.hide();
        }
    });
});
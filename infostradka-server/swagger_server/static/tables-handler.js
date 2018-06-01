$(document).ready(function() {
    table_events_handlers();

    $('.add-main-btn').click(function(event){
        tbody = $(event.target).parent().parent().parent().parent().find('tbody').first();
        tbody.append('<tr style="cursor: move;"><td class="td-move-ico"></td><td><select name="content_type">'+
        '<option value="www">Strona WWW</option><option value="file">Zapisany plik</option>'+
        '<option value="yt">Wideo z Youtube</option></select></td><td><input name="url" value="" style="">'+
        FILES_HTML +
        '</td><td><input name="start_stop_time" type="text"></td><td><input name="duration" value="">'+
        '</td><td><img class="delete-btn" src="/static/delete.png"></td></tr>')

        // renew table handlers
        table_events_handlers();
    });

    $('#main_content_change').submit(function(event){
        var form = $(event.target);
        var types = form.find('select[name="content_type"]');
        var urls = form.find('input[name="url"]');
        var hashes = form.find('select[name="file_hash"]');
        var start_stop_times = form.find('input[name="start_stop_time"]');
        var durations = form.find('input[name="duration"]')

        var req = [];

        types.each(function(x, y){
            var dates = start_stop_times[x].value.split(" - ");
            req.push({
                "content": {
                    "source": types[x].value == 'file' ? hashes[x].value : urls[x].value,
                    "subtitles": ""
                },
                "duration": durations[x].value,
                "since": dates[0],
                "type": types[x].value,
                "until": dates[1]
            });
        });

        $.ajax({
            type: "POST",
            url: "/v1/manager/main_content",
            data: JSON.stringify(req),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function(msg) {
                alert("Zapisano!");
            },
            failure: function(errMsg) {
                alert(errMsg);
            }
        });

        return false;
    });
});

function table_events_handlers(){
    // rows change
    $("#settings-tbl").tableDnD();

    // date-time range picker
    $('input[name="start_stop_time"]').daterangepicker({
        timePicker: true,
//        startDate: moment().startOf('hour'),
//        endDate: moment().startOf('hour').add(32, 'hour'),
        locale: {
          format: 'Y-MM-DD HH:mm'
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

    // delete row
    $('.delete-btn').click(function(event){
        $(event.target).parent().parent().remove()
    });
}
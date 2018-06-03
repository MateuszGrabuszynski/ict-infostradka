$(document).ready(function() {
    $('.delete-file-btn').click(function(event){
        var hash = $(event.target).attr('hash');

        if(!confirm("Usunąć?")){
            return
        }

        $.ajax({
            type: "DELETE",
            url: "/v1/manager/files/" + hash,
            complete: function(jqXHR) {
                $(event.target).parent().remove();
                alert("Usunięto!");
            }
        });
    });
});
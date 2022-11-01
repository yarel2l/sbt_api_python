var url_profile_endpoint = document.currentScript.dataset.url;
var user_tz = document.currentScript.dataset.utz;
var modal_tz = new bootstrap.Modal(document.getElementById('timezone_modal'));
const tzone = Intl.DateTimeFormat().resolvedOptions().timeZone;


var timezone_input = $('#id_timezone_input');
timezone_input.val(tzone); // Select the option with a value of '1'
timezone_input.trigger('change');
if (user_tz !== tzone) {
   modal_tz.show();
}

$('#save_timezone_btn').click(function (e) {
    var data = {
        "timezone": timezone_input.val()
    };
    $.ajax({
        type: 'PATCH',
        url: url_profile_endpoint,
        contentType: 'application/json',
        data: JSON.stringify(data), // access in body
    }).done(function () {
        sessionStorage.setItem('timezone', tzone);
        modal_tz.hide();
        Swal.fire({
            text: gettext('Timezone updated successfully'),
            icon: "success",
            buttonsStyling: false,
            confirmButtonText: gettext("Ok, got it!"),
            customClass: {
                confirmButton: "btn btn-primary"
            }
        }).then(function (r) {
             window.location.reload();
        });
    }).fail(function (msg) {
        Swal.fire({
            text: gettext("Error updating timezone"),
            icon: "error",
            buttonsStyling: false,
            confirmButtonText: gettext("Ok"),
            customClass: {
                confirmButton: "btn btn-primary"
            }
        }).then(function (r) {
             window.location.reload();
        });
    });
});
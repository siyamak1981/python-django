
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function () {
    var $myForm = $('.eagle')
    $myForm.submit(function (event) {
        event.preventDefault()
        var $formData = $(this).serializer()
        var $thisURL = $myForm.attr('data-url') || window.location.href
        $.ajax({
            method: "Post",
            url: $thisURL,
            data: $formData,
            success: handleFormsSuccess,
            error: handleFormError,

        })
    })
    function handleFormsSuccess(data, textstatus, _jqXHR) {
        $("div.eagle-on").css("display", "block")
        $myForm.reset();

    }

    function handleFormError(jqXHR, textstatus, errorThrown) {
        $("div.eagle-off").css("display", "block")
    }
})

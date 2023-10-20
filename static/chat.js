$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);
        $.ajax({
            url: '/upload',
            type: 'POST',
            data: formData,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.success) {
                    $('#pdf-text').text(data.text);
                } else {
                    alert('Error: ' + data.error);
                }
            }
        });
    });
});

$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus, jqXHR) {
    $('DIV#hello').append(data.hello);
});
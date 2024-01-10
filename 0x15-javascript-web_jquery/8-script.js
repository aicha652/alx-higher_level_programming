$.get('https://swapi-api.alx-tools.com/api/films/?format=json', {"results[]": ["title"]}, function (data, textStatus, jqXHR) {
    $.each(data.results, function(index, item) { // Iterate over the "results" array
        // Append the title to the UL with ID "list_movies"
        $('UL#list_movies').append("<li>"+item.title+"</li>");
    });
});
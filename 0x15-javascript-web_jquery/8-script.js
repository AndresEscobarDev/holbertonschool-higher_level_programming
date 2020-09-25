$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (i, value) {
    $('<li>' + value.title + '</li>').appendTo('#list_movies');
  });
});

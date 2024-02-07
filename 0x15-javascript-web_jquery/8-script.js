$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  success: function (response) {
    for (const i of response.results) {
      $('#list_movies').append('<li>' + i.title + '</li>');
    }
  },

  error: function (xhr, status, error) {
    console.error(error);
  }
});

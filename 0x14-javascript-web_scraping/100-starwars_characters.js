#!/usr/bin/node
const request = require('request');
const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(urlFilm, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const datas = JSON.parse(body).characters;
    for (const urlChr of datas) {
      request.get(urlChr, (err, response, body) => {
        if (err) {
          console.error(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});

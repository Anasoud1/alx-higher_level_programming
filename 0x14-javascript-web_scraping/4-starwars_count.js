#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const pId = 'https://swapi-api.alx-tools.com/api/people/18/';
let datas;
let i = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    datas = JSON.parse(body);
    for (const data of datas.results) {
      if (data.characters.includes(pId)) {
        i += 1;
      }
    }
    console.log(i);
  }
});

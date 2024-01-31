#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const pId = 'https://swapi-api.alx-tools.com/api/people/18/';
let i = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const datas = JSON.parse(body).results;
    datas.forEach(op => {
      if (op.characters.includes(pId)) {
        i++;
      }
    });
    console.log(i);
  }
});

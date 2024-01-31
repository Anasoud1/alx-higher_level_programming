#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const pId = '18';
let i = 0;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const datas = JSON.parse(body).results;
    datas.forEach(op => {
      op.characters.forEach(chr => {
        if (chr.includes(pId)) {
          i++;
	}
      });
    });
    console.log(i);
  }
});

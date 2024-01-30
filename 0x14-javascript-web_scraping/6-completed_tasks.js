#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let j = 0;
let i = 0;
let count;
const dic = {};

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const datas = JSON.parse(body);
    while (i < datas.length) {
      j += 1;
      count = 0;
      while (datas[i].userId === j && i !== datas.length - 1) {
        if (datas[i].completed === true) {
          count += 1;
        }
        i += 1;
      }

      dic[j] = count;
      if (i === datas.length - 1) break;
      // i += 1
    }
    console.log(dic);
  }
});

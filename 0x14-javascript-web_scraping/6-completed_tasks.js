#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dic = {};

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed === true) {
        if (dic[todo.userId] === undefined) {
          dic[todo.userId] = 1;
        } else {
          dic[todo.userId]++;
        }
      }
    }
    console.log(dic);
  }
});

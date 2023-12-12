#!/usr/bin/node
const list = require('./100-data.js').list;
const newList = list.map((x, idx) => x * idx);
console.log(list);
console.log(newList);

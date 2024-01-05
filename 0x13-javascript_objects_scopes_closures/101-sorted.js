#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
let k = 0;
let array;
for (const i in dict) {
  array = [];
  k = 0;
  for (const j in dict) {
    if (dict[i] === dict[j]) {
      array[k] = j;
      k++;
    }
  }
  newDict[dict[i]] = array;
}
console.log(newDict);

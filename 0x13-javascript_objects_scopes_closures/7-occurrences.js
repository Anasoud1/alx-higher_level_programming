#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let s = 0;
  for (let i = 0; list[i]; i++) {
    if (searchElement === list[i]) {
      s++;
    }
  }
  return s;
};

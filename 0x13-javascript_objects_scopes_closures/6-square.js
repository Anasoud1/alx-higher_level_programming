#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log('C'.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;

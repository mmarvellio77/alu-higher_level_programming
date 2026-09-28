#!/usr/bin/node
const Square = require('./5-square');

class Square2 extends Square {
  charPrint (c = 'X') {
    if (this.width === undefined || this.height === undefined) return;
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square2;

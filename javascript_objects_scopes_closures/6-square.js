#!/usr/bin/node
const newSquare = require('./5-square');


class Square extends newSquare {
  charPrint (c) {
    const chr = c || 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}

module.exports = Square;


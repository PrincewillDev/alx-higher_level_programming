#!/usr/bin/node

const ImportSquare = require('./5-square.js');

class Square extends ImportSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
  }
}
module.exports = Square;

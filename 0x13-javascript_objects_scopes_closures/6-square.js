#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) c = 'X';
    for (let i = 1; i <= this.width; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

#!/usr/bin/node
const ImportSquare = require('./5-square');
class Square extends ImportSquare {
  charPrint (c) {
    if (!c) c = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;

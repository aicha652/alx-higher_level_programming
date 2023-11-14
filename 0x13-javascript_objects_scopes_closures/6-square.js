#!/usr/bin/node
const ImportSquare = require('./5-square');
class Square extends ImportSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('C');
        }
        console.log();
      }
    }
  }
}
module.exports = Square;
#!/usr/bin/node
const sqr = require('./5-square');

class Square extends sqr {
  charPrint (c) {
    let char = 'c';
    if (c === undefined){
      char = 'X';
    }
    console.log((char.repeat(this.width) + '\n').repeat(this.height - 1) + char.repeat(this.width));
  }
}
module.exports = Square;

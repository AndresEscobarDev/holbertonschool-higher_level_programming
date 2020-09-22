#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (w) {
    super(w, w);
  }
}
module.exports = Square;

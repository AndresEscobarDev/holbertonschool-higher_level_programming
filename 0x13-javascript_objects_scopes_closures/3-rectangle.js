#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((Number.isInteger(w + h)) && (w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
  }
}
module.exports = Rectangle;

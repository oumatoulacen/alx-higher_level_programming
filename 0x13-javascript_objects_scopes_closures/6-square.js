#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let a = '';
      for (let j = 0; j < this.width; j++) {
        a += 'X';
      }
      console.log(a);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  charPrint (c) {
    if (c === undefined || !c) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;

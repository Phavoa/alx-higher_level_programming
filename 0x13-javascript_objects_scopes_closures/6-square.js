#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};


const s1 = new Square(4);
s1.charPrint();

s1.charPrint('C');
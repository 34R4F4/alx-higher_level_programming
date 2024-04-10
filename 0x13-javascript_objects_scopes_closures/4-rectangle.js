#!/usr/bin/node
// a class Rectangle that defines a rectangle
// If w or h is equal to 0 or not a positive integer, create an empty object
// Create an instance method called print() that prints the rectangle using the character X

class Rectangle {
  constructor (w, h) {
    // Initialize the instance attributes
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let c = 0; c < this.height; c++) {
      let row = '';
      for (let r = 0; r < this.width; r++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  // instance method called rotate() that exchanges the width and the height of the rectangle
  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  // instance method called double() that multiples the width and the height of the rectangle by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;

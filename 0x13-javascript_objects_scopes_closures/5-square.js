#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js

// inherits from Rectangle
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // calling constructor of Rectangle using super()
    super(size, size);
  }
}

// Export the Square class
module.exports = Square;

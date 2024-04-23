#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;

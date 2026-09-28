#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number') return;
    if (!Number.isInteger(w) || !Number.isInteger(h)) return;
    if (w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;

class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number') return;
    if (!Number.isInteger(w) || !Number.isInteger(h)) return;
    if (w <= 0 || h <= 0) return;
    this.width = w;
    this.height = h;
  }

  print () {
    if (this.width === undefined || this.height === undefined) return;
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

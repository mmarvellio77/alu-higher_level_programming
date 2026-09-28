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

  rotate () {
    if (this.width === undefined || this.height === undefined) return;
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    if (this.width === undefined || this.height === undefined) return;
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;

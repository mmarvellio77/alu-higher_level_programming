exports.converter = function (base) {
  if (base < 2 || base > 36) {
    return function (n) { return ''; };
  }
  return function toBase (n) {
    if (n < 0) return '-' + toBase(-n);
    if (n < base) return '0123456789abcdefghijklmnopqrstuvwxyz'[n];
    return toBase(Math.floor(n / base)) + '0123456789abcdefghijklmnopqrstuvwxyz'[n % base];
  };
};

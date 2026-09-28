# 0x0D. JavaScript - Objects, Scopes and Closures

Tasks written in JavaScript (Node.js) for the **ALU Higher Level
Programming** — Objects, Scopes and Closures project.

## Files

| File                    | Description                                                                       |
| ----------------------- | --------------------------------------------------------------------------------- |
| `0-rectangle.js`        | Empty `Rectangle` class exported with `module.exports`                             |
| `1-rectangle.js`        | `Rectangle` storing `width` and `height` from constructor arguments `w` and `h`   |
| `2-rectangle.js`        | `Rectangle` that stays an empty object when `w` or `h` is not a positive integer   |
| `3-rectangle.js`        | Adds `print()` to draw the rectangle with the character `X`                       |
| `4-rectangle.js`        | Adds `rotate()` (swaps `w`/`h`) and `double()` (multiplies both by 2)              |
| `5-square.js`           | `Square extends Rectangle` built with `super(size, size)`                          |
| `6-square.js`           | Adds `charPrint(c)` to draw the square with a custom character, defaulting to `X`  |
| `7-occurrences.js`      | `nbOccurences(list, searchElement)` counting occurrences in a list                 |
| `8-esrever.js`          | `esrever(list)` returning a reversed copy without using the built-in `reverse`    |
| `9-logme.js`            | `logMe(item)` logging the number of arguments already printed and the new value   |
| `10-converter.js`       | `converter(base)` returning a function that converts a base 10 number to `base`    |

## Usage

```console
$ node -e "const R = require('./4-rectangle'); const r = new R(2, 3); r.double(); r.rotate(); r.print();"
XXXXXX
XXXXXX
XXXXXX
XXXXXX
```

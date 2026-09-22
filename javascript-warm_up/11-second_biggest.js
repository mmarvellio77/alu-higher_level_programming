#!/usr/bin/node
const args = process.argv.slice(2).map(Number).sort((a, b) => b - a);
console.log(args[1] !== undefined ? args[1] : 0);

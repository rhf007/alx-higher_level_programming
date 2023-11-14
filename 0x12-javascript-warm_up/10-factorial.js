#!/usr/bin/node

const process = require('process');
const args = process.argv;

function factorial (a) {
  if (isNaN(a) || a === 1 || a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
const result = factorial(parseInt(args[2]));
console.log(result);

#!/usr/bin/node

const process = require('process');
const args = process.argv;

function add (a, b) {
  return a + b;
}

const result = add(parseInt(args[2]), parseInt(args[3]));
console.log(result);

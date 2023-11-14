#!/usr/bin/node

const process = require('process');
const args = process.argv;

if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    let r = '';
    for (let j = 0; j < parseInt(args[2]); j++) {
      r += 'X';
    }
    console.log(r);
  }
}

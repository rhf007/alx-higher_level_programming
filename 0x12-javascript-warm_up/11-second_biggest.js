#!/usr/bin/node

const process = require('process');
const args = process.argv;
let argv = args.slice(2).map(Number);
argv = argv.sort().reverse();
if (argv.length <= 2) {
  console.log(0);
} else {
  console.log(parseInt(argv[1]));
}

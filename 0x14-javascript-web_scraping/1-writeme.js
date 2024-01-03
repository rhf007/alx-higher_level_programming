#!/usr/bin/node

const file = require('fs');
const path = process.argv[2];
const str = process.argv[3];

file.writeFile(path, str, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});

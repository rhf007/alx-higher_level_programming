#!/usr/bin/node

const file = require('fs');
const path = process.argv[2];

file.readFile(path, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});

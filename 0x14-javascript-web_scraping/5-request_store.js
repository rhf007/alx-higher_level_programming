#!/usr/bin/node

const f = require('fs');
const r = require('request');
const url = process.argv[2];
const file = process.argv[3];

r.get(url, function (err, res, bod) {
  if (err) {
    console.log(err);
  } else {
    f.writeFile(file, bod, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});

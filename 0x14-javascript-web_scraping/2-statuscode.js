#!/usr/bin/node

const url = require('request');
const url2 = process.argv[2];

url.get(url2, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});

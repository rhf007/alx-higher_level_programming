#!/usr/bin/node

const r = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

r.get(url, function (err, res, bod) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(bod);
    const movies = data.results.filter(movie =>
      movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    );
    console.log(movies.length);
  }
});

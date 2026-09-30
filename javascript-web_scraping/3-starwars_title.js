#!/usr/bin/node
const request = require('request');

const id = process.argv[2];

const getFilm = (filmId) => new Promise((resolve, reject) => {
  request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (err, response, body) => {
    if (err) {
      reject(err);
      return;
    }
    resolve(JSON.parse(body));
  });
});

getFilm(id)
  .then((film) => console.log(film.title))
  .catch((err) => console.error(err.message));

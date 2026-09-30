#!/usr/bin/node
const request = require('request');

const WEDGE_ANTILLES_ID = 18;
const url = process.argv[2];

const getFilms = (apiUrl) => new Promise((resolve, reject) => {
  request.get(apiUrl, (err, response, body) => {
    if (err) {
      reject(err);
      return;
    }
    if (response.statusCode !== 200) {
      reject(new Error(`${response.statusCode}: request failed`));
      return;
    }
    resolve(JSON.parse(body));
  });
});

getFilms(url)
  .then((data) => {
    const count = data.results.filter((film) =>
      film.characters.some((character) => character.endsWith(`/${WEDGE_ANTILLES_ID}/`))
    ).length;
    console.log(count);
  })
  .catch((err) => console.error(err.message));

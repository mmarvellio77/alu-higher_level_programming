#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

const getStatusCode = (target) => new Promise((resolve, reject) => {
  request.get(target, (err, response) => {
    if (err) {
      reject(err);
      return;
    }
    resolve(response.statusCode);
  });
});

getStatusCode(url)
  .then((code) => console.log(`code: ${code}`))
  .catch((err) => console.error(err.message));
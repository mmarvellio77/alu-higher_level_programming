#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

const fetchBody = (target) => new Promise((resolve, reject) => {
  request.get(target, (err, response, body) => {
    if (err) {
      reject(err);
      return;
    }
    if (response.statusCode !== 200) {
      reject(new Error(`${response.statusCode}: request failed`));
      return;
    }
    resolve(body);
  });
});

fetchBody(url)
  .then((body) => {
    fs.writeFileSync(filePath, body, 'utf-8');
  })
  .catch((err) => console.error(err.message));

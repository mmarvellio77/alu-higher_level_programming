#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

const getTodos = (apiUrl) => new Promise((resolve, reject) => {
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

getTodos(url)
  .then((todos) => {
    const completed = {};
    todos
      .filter((todo) => todo.completed)
      .forEach((todo) => {
        const userId = todo.userId;
        completed[userId] = (completed[userId] || 0) + 1;
      });
    console.log(completed);
  })
  .catch((err) => console.error(err.message));

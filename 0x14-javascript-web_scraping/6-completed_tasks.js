#!/usr/bin/node
/* Write a script that computes the number of tasks completed by user id.

The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only print users with completed task
You must use the module request
*/
const args = process.argv;
const request = require('request');

request(args[2], (err, code, body) => {
  if (err) { console.error(err); } else {
    const users = {};
    for (const element in JSON.parse(body)) {
      if (JSON.parse(body)[element].completed) {
        users[JSON.parse(body)[element].userId] = (users[JSON.parse(body)[element].userId] || 0) + 1;
      }
    }
    console.log(users);
  }
});

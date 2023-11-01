#!/usr/bin/node
/* Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request
*/
const args = process.argv;
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + args[2], (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    for (const character of JSON.parse(body).characters) {
      request(character, (err, code, body) => {
        if (err) { console.error(err); } else { console.log(JSON.parse(body).name); }
      });
    }
  }
});

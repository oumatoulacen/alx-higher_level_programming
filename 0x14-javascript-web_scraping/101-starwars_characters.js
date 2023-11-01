#!/usr/bin/node
/*
Write a script that prints all characters of a Star Wars movie:

The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line in the same order of the list “characters” in the /films/ response
You must use the Star wars API
You must use the module request
*/
const argv = process.argv;
const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

const request = require('request');

request(urlMovie, function (error, response, body) {
  if (error == null) {
    const fbody = JSON.parse(body);
    const characters = fbody.characters;

    if (characters && characters.length > 0) {
      const limit = characters.length;
      CharRequest(0, characters[0], characters, limit);
    }
  } else {
    console.log(error);
  }
});
function CharRequest (idx, url, characters, limit) {
  if (idx === limit) { return; }
  request(url, function (error, response, body) {
    if (!error) {
      const rbody = JSON.parse(body);
      console.log(rbody.name);
      idx++;
      CharRequest(idx, characters[idx], characters, limit);
    } else {
      console.error('error:', error);
    }
  });
}

/* const args = process.argv;
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request);

request('https://swapi-api.alx-tools.com/api/films/' + args[2],
  async function test (err, code, body) {
    if (err) {
      console.error(err);
    } else {
      for (const character of JSON.parse(body).characters) {
        try {
          const response = await requestPromise(character, { json: true });
          console.log(response.body.name);
        } catch (err) {
          console.log(err);
        }
      }
    }
  });
*/

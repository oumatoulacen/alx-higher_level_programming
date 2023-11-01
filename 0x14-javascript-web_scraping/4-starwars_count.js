#!/usr/bin/node
/* Write a script that prints the number of movies where
the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API:
https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');
const ApiUrl = process.argv[2];
const UrlChar = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(ApiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body).results;
    let num = 0;
    data.forEach(element => {
      if (element.characters.includes(UrlChar)) num++;
    });
    console.log(num);
  }
});

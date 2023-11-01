#!/usr/bin/node
/* Write a script that prints the number of movies where
the character “Wedge Antilles” is present.

The first argument is the API URL of the Star wars API:
https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const args = process.argv;
const request = require('request');

request(args[2], (err, code, body) => {
  if (err) {
    console.error(err);
  } else {
    let n = 0;
    for (const film in JSON.parse(body).results) {
      for (const character in JSON.parse(body).results[film].characters) {
        if (JSON.parse(body).results[film].characters[character].includes('18')) { n += 1; }
      }
    }
    console.log(n);
  }
});

// const request = require('request');
// const ApiUrl = process.argv[2];
// const UrlChar = 'https://swapi-api.alx-tools.com/api/people/18/';

// request.get(ApiUrl, (error, response, body) => {
//   if (!error && response.statusCode === 200) {
//     const data = JSON.parse(body).results;
//     let num = 0;
//     data.forEach(element => {
//       if (element.characters.includes(UrlChar)) {
//         num++;
//       }
//     });
//     console.log(num);
//   } else {
//     console.log(error);
//   }
// });

#!/usr/bin/node

const fs = require('fs');
const filepath = process.argv[2];
const content = process.argv[3];

if (!filepath) {
  console.log('Please specify a path to a file');
  process.exit(1);
}

fs.writeFile(filepath, content, 'utf8', (err, result) => {
  if (err) {
    console.log(err);
  } else {
    console.log(result);
  }
});

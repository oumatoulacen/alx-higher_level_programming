#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.log('Please provide a file path as an argument.');
  process.exit(1);
}

// Reading the file content in utf-8 encoding
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  else {
    console.log(data);
  }
});

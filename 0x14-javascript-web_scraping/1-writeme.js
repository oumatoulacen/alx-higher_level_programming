#!/usr/bin/node
/*
Write a script that writes a string to a file.

The first argument is the file path
The second argument is the string to write
The content of the file must be written in utf-8
If an error occurred during while writing, print the error object
*/
const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.log('Please provide a file path and content to write as arguments.');
  process.exit(1);
}

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});

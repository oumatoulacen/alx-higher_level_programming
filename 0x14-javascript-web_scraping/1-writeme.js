#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
  console.log('Please provide a file path and content to write as arguments.');
  process.exit(1);
}

// Writing the content to the file in utf-8 encoding
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log(contentToWrite);
  }
});

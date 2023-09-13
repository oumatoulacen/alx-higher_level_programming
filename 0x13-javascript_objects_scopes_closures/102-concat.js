#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: node 102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const [, , file1Path, file2Path, destinationPath] = process.argv;

fs.readFile(file1Path, 'utf8', (err1, data1) => {
  if (err1) {
    process.exit(1);
  }

  fs.readFile(file2Path, 'utf8', (err2, data2) => {
    if (err2) {
      process.exit(1);
    }

    const concatenatedData = data1 + data2;

    fs.writeFile(destinationPath, concatenatedData, 'utf8', (err3) => {
      if (err3) {
        console.error(`Error writing to ${destinationPath}: ${err3}`);
        process.exit(1);
      }
    });
  });
});

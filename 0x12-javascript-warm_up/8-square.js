#!/usr/bin/node

const convertedArg = parseInt(process.argv[2]);

if (isNaN(convertedArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < convertedArg; i++) {
    let row = '';
    for (let j = 0; j < convertedArg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}

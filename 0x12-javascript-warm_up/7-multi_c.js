#!/usr/bin/node

const convertedArg = parseInt(process.argv[2]);

if (isNaN(convertedArg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < convertedArg; i++) {
    console.log('C is fun');
  }
}

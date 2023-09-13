#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const tmp = list.map((v, x) => v * x);

console.log(tmp);

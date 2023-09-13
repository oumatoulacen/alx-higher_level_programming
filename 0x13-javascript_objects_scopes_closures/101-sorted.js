#!/usr/bin/node

const dict = require('./101-data').dict;
const values = Object.values(dict);
const arr = [];
const obj = {};
values.forEach(value => {
  if (!arr.includes(value)) {
    obj[value] = [];
  }
});
const keys = Object.keys(dict);

keys.forEach(key => {
  const value = dict[key];
  const len = obj[value].length;
  obj[String(value)][len] = key;
});

console.log(obj);

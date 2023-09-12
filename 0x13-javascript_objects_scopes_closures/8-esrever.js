#!/usr/bin/node

exports.esrever = function (list) {
  const tmp = [];
  for (let i = list.length; i > 0; i--) {
    tmp[list.length - i] = list[i - 1];
  }
  return tmp;
};

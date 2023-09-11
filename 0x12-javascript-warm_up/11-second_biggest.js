#!/usr/bin/node

function secondBiggest (list) {
  let previous = 0;
  let max = 0;

  if (list.length <= 2) {
    return (0);
  } else {
    for (let i = 2; i < list.length; i++) {
      if (+list[i] > max) {
        max = list[i];
      }
    }
    for (let j = 2; j < list.length; j++) {
      if (+list[j] > previous && list[j] < max) {
        previous = list[j];
      }
    }
  }
  return previous;
}
console.log(secondBiggest(process.argv));

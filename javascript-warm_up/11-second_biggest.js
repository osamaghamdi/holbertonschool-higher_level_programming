#!/usr/bin/node
const arg = process.argv;
const size = arg.length;
if (size <= 3) {
  console.log(0);
} else {
  arg.sort(function (a, b) {
    return a - b;
  });
  const secondBiggest = arg[size - 2];
  console.log(secondBiggest);
}

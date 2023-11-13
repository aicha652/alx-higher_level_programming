#!/usr/bin/node
let result;
if (process.argv.length <= 2) {
  result = 0;
} else {
  const numbers = process.argv.slice(2).map(Number);
  numbers.sort((a, b) => b - a);
  result = numbers[1] || 0;
}
console.log(result);

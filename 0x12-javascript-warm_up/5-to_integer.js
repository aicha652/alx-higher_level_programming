#!/usr/bin/node
let result;
let convert;
if (process.argv.length === 2) {
  result = 'Not a number';
} else if (process.argv[2]) {
  convert = parseInt(process.argv[2]);
  if (isNaN(parseInt(process.argv[2]))) {
    result = 'Not a number';
  } else {
    result = 'My number: ' + convert;
  }
}
console.log(result);

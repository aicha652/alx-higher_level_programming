#!/usr/bin/node
let arg;
if (!process.argv[2]) {
  arg = 'No argument';
} else {
  arg = process.argv[2];
}
console.log(arg);

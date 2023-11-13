#!/usr/bin/node
const { argv } = require('node:process');
if (!argv[2]) {
  arg = 'No argument';
} else {
  arg = argv[2];
}
console.log(arg);

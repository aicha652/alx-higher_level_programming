#!/usr/bin/node
// First argument is the file path
// The second argument is the file’s character encoding
// The third argument is is the call back function
// which takes the error as the parameter
const fs = require('fs');
const process = require('process');
fs.readFile(process.argv[2], 'utf-8', (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});

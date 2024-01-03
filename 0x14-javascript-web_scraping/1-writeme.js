#!/usr/bin/node
// Import FileSystem
const fs = require('fs');

const process = require('process');

// Regular Content of the file
const filecontent = process.argv[3];

// 1. Write a file with UTF-8
// The first argument is the file path
// The second argument is the string to write
// The content of the file must be written in utf-8
fs.writeFile(process.argv[2], filecontent, 'utf-8', (err) => {
  if (err) throw err;
});

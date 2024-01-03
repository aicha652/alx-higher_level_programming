#!/usr/bin/node
// Import FileSystem
const fs = require('fs');

const process = require('process');

// Regular Content of the file
const filecontent = 'Python is cool';

// 1. Write a file with UTF-8
fs.writeFile(process.argv[2], filecontent, 'utf-8', (err) => {
  if (err) throw err;
});

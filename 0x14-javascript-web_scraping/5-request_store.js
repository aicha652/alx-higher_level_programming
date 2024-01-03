#!/usr/bin/node
// script that gets the contents of a
// webpage and stores it in a file

// import the request module
const request = require('request');

// import the process module
const process = require('process');

// import FileSystem
const fs = require('fs');

// extract the url from the command-line arguments
const url = process.argv[2];

// extract the file path from the cmd-line arguemnts
const filename = process.argv[3];

request(url, (error, response, body) => {
  if (error) throw error;
  else {
    fs.writeFileSync(filename, body, 'utf-8', (err) => {
      if (err) throw err;
    });
  }
});

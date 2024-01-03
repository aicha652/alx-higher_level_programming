#!/usr/bin/node
// script that display the status code of a GET request

// import the request module
const request = require('request');

// import the process module
const process = require('process');

// The first argument is the URL to request (GET)
request(process.argv[2])
  .on('response', function (response) {
    console.log('code:', response.statusCode);
  });

#!/usr/bin/node
// script that prints the title of a Star Wars movie
// where the episode number matches a given integer

// import the request module
const request = require('request');

// import the process module
const process = require('process');

// extract the movie ID from the command-line arguments
const movieId = process.argv[2];

// construct the API URL by appending the movie ID to the base URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to fetch information about the film
request(url, (error, response, body) => {
  if (error) throw error;
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});

#!/usr/bin/node

// Script that prints all characters of a Star Wars movie
// Character names are displayed in 
// the same order of the list “characters”
// in the films response

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(error);
    return;
  }

  const chars = JSON.parse(response.body).characters;
  const charPromises = chars.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, response) => {
        if (error) {
          reject(error);
        } else {
          resolve(JSON.parse(response.body).name);
        }
      });
    });
  });

  Promise.all(charPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
});

#!/usr/bin/node

// Script that reads from a file and displays the contents on standard output.

const fileSystem = require('fs');
const path = require('path');

function processCommandlineArguments() {
  if (process.argv.length !== 3) {
    console.error(`Usage: ${path.basename(process.argv[1])} <filename>`);
    return 1;
  }

  const filename = process.argv[2];
  fileSystem.readFile(filename, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(data);
  });
}

processCommandlineArguments();

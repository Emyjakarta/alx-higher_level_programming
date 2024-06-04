#!/usr/bin/node

// Script that writes the contents received on the CLI to a file.

const fileSystem = require('fs');
const path = require('path');

function writeOnToFile () {
  if (process.argv.length !== 4) {
    console.error(`Usage: ${path.basename(process.argv[1])} <filename> <data>`);
    return;
  }

  const filename = process.argv[2];
  const data = process.argv[3];
  fileSystem.writeFile(filename, data, (err) => {
    if (err) {
      console.error(err);
    }
  });
}

writeOnToFile();

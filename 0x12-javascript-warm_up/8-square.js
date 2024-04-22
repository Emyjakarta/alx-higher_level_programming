#!/usr/bin/node

const size = parseInt(process.argv[2]);

if (!size) console.log('Missing size');
else {
  for (let q = 0; q < size; q++) {
    let line = '';
    for (let r = 0; r < size; r++) {
      line += 'X';
    }
    console.log(line);
  }
}

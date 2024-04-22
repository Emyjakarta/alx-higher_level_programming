#!/usr/bin/node

const numOfOccurrences = parseInt(process.argv[2]);

if (!isNaN(numOfOccurrences)) {
  for (let i = 0; i < numOfOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}

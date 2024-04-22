#!/usr/bin/node

function secBig (numbers) {
  if (numbers.length <= 1) {
    return 0;
  }

  let max = -Infinity;
  let secMax = -Infinity;

  for (let i = 0; i < numbers.length; i++) {
    const num = parseInt(numbers[i]);
    if (num > max) {
      secMax = max;
      max = num;
    } else if (num > secMax && num !== max) {
      secMax = num;
    }
  }

  return secMax;
}

const args = process.argv.slice(2);
console.log(secBig(args));

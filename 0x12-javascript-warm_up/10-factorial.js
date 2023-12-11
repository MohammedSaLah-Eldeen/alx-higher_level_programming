#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number === 1) return 1;

  return number * factorial(number - 1);
}

const fact = factorial(parseInt(process.argv[2]));
console.log(fact);


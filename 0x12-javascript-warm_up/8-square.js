#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) console.log('Missing size');
else {
  const size = parseInt(process.argv[2]);
  for (let v = 1; v <= size; v++) {
    for (let h = 1; h <= size; h++) {
      console.log('X')
    }
  }
}

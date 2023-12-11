#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) console.log('Missing number of occurrences');
else {
  for (let c = 1; c <= parseInt(process.argv[2]); c++) {
    console.log('C is fun');
  }
}

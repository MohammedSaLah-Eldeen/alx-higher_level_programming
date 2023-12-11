#!/usr/bin/node

let parsedNumber = parseInt(process.argv[2]);
if (isNaN(parsedNumber) || parsedNumber === undefined) console.log('Not a Number');
else console.log('My number: ' + parsedNumber);

#!/usr/bin/node

let parsedNumber = parseInt(process.argv[2]);
if (!parsedNumber) console.log('Not a Number');
else console.log(parsedNumber);

#!/usr/bin/node

if (process.argv.length <= 3) console.log('0');
else {
  const arr = process.argv.slice(2).map(Number).sort().pop();
  const second = arr[-1];
  console.log(second);
}

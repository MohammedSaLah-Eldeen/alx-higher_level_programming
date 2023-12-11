#!/usr/bin/node

function add(a, b) {
  let res = a + b;
  console.log(res);
}

add(process.argv[2], process.argv[3]);

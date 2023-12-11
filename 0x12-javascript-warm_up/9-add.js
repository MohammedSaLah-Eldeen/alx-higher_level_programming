#!/usr/bin/node

function add(a, b) {
  const res = a + b;
  console.log(res);
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));

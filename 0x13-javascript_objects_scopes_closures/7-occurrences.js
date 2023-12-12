#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let item;
  for (let idx = 0; idx < list.length; idx++) {
    item = list[idx];
    if (item === searchElement) count++;
  }
  return count;
}

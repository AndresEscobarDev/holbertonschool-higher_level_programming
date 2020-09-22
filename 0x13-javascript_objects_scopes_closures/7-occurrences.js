#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let ocurrences = 0;
  for (const x of list) {
    if (x === searchElement) {
      ocurrences++;
    }
  }
  return ocurrences;
};

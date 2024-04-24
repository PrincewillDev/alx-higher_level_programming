#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const arryLength = list.length;
  for (let i = 0; i < arryLength; i++) {
    if (searchElement === list[i]) {
      count += 1;
    }
  }

  return count;
};

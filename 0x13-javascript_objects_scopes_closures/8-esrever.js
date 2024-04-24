#!/usr/bin/node
exports.esrever = function (list) {
    reversedList = [];
    const arryLength = list.length;
    for (let i = arryLength - 1; i >= 0; i--){
    reversedList.push(list[i]);
  }
  return reversedList;
};

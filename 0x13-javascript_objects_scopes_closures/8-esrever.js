#!/usr/bin/node

exports.esrever = function (list) {
  const revlist = [];
  for (let i = list.length - 1, j = 0; i >= 0 && j < list.length; i--, j++) {
    revlist[j] = list[i];
  }
  return revlist;
};

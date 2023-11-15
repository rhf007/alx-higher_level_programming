#!/usr/bin/node

// thats when you know you should read the doc again:
/* By default toString() takes no parameters. However, objects that inherit
   from Object may override it with their own implementations that do take
   parameters. For example, the Number.prototype.toString() and
   BigInt.prototype.toString() methods take an optional radix parameter. */
exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};

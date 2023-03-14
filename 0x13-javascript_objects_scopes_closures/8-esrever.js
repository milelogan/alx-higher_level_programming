#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (arr, curr) {
    arr.push(curr);
    return arr;
  }, []);
};

#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((counter, current) => current === searchElement ? counter + 1 : counter, 0);
};

#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement)  {
  return (list.reduce((i, value) => i + (value === searchElement), 0));
};


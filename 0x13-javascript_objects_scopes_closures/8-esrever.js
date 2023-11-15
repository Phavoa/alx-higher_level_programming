#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    i++;
    len--;
  }
  return list;
};

console.log(esrever([1, 2, 3, 4, 5]));
console.log(esrever(["School", 89, { id: 12 }, "String"]));
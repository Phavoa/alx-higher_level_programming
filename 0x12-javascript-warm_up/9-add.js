#!/usr/bin/node
function add(a, b) {
  return (a + b);
}


const argv = process.argv;
const num1= parseFloat(argv[2]);
const num2= parseFloat(argv[3]);
console.log(add(num1, num2))
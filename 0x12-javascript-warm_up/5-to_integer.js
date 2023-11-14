#!/usr/bin/node

const argv = process.argv;

const num = parseFloat(argv[2]);

if (Number.isInteger(num))
{
  console.log(`My number: ${num}`);
  
}
else {
  console.log("Not a number")
}
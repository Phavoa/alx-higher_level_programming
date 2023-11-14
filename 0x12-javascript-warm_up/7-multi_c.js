#!/usr/bin/node
const argv = process.argv;
const num = parseFloat(argv[2]);
if (Number.isInteger(num)) {
  for (i = 0; i < num; i++) {
    console.log("C is fun");
  }
} else {
  console.log("Missing number of occurrences")
}
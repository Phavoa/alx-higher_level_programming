#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let first = parseInt(argv[2]);
  let second = parseInt(argv[2]);

  for (let i = 3; i < argv.length; i++) {
    const num = parseInt(argv[i]);
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num < first) {
      second = num;
    }
  }

  console.log(second);
}
#!/usr/bin/node
function factorial (n) {
  if (n === 0) { return 1; }
  return n * factorial(n - 1);
}
if (process.argv.length < 3) {
  console.log('1');
} else {
  console.log(factorial(parseInt(process.argv[2])));
}

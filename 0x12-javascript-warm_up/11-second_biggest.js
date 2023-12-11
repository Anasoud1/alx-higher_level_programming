#!/usr/bin/node
const argv = process.argv;
const length = argv.length;
if (length <= 3) {
  console.log('0');
} else {
  let max = 0; let secMax = 0; let tmp;
  for (let i = 2; argv[i]; i++) {
    if (secMax < parseInt(argv[i])) {
      secMax = parseInt(argv[i]);
    }
    if (max < secMax) {
      tmp = max;
      max = secMax;
      secMax = tmp;
    }
  }
  console.log(secMax);
}

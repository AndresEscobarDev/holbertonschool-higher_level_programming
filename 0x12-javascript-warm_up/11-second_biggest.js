#!/usr/bin/node
let n = 0;
if (process.argv.length > 3) {
  let m = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > m) {
      n = m;
      m = process.argv[i];
    }
  }
  console.log(n);
} else {
    console.log(0);
}

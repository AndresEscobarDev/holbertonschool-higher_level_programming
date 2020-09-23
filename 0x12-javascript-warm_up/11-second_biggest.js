#!/usr/bin/node
let n = parseInt(process.argv[3]);
if (process.argv.length > 3) {
  let m = parseInt(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
      if (parseInt(process.argv[i]) > m) {
        n = m;
        m = parseInt(process.argv[i]);
    }
  }
  console.log(n);
} else {
  console.log(0);
}

#!/usr/bin/node
console.log((process.argv.length < 3) ? 0 : process.argv.slice(2).sort ((a, b) => b - a)[1])

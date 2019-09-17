#!/usr/bin/node
const x = process.argv[2];
console.log(isNaN(x) ? 'Not a number' : 'My number: ' + x);

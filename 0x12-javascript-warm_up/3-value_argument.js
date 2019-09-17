#!/usr/bin/node
let firstArg = process.argv[2];
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}

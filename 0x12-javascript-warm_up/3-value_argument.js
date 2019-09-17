#!/usr/bin/node
let argCount = process.argv.length;
let firstArg = process.argv[2];
if (argCount === 2) {
  console.log('No argument');
} else {
  console.log(firstArg);
}

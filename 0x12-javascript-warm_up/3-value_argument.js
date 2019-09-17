#!/usr/bin/node
const argCount = process.argv.length;
const firstArg = process.argv[2];
if (argCount === 2) {
  console.log('No argument');
} else {
  console.log(firstArg);
}

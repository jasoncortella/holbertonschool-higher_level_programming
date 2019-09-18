#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0] === undefined) {
  console.log('0');
} else if (args[1] === undefined) {
  console.log('0');
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}

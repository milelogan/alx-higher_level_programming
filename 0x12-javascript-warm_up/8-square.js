#!/usr/bin/node
// a script that prints a square

let args = process.argv[2];
if (isNaN(Number(args))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args); i++) {
    console.log('X'.repeat(args));
  }
}

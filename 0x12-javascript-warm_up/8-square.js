#!/usr/bin/node
if (!process.argv[2]) {
  console.log('Missing size');
} else if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    for (let j = 0; j < process.argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}

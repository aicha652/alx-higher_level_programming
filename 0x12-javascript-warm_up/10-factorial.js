#!/usr/bin/node
function factoriel (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factoriel(n - 1);
}
const number = process.argv[2];
console.log(factoriel(number));

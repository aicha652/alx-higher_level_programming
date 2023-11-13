#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const [,, arg1, arg2] = process.argv;
add(parseInt(arg1), parseInt(arg2));

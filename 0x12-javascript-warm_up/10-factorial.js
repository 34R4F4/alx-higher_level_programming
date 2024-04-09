#!/usr/bin/node
/* script computes and prints a factorial */
const x = Number.parseInt(process.argv[2]);
function factoria (n) {
  if (n === 0 || Number.isNaN(n)) {
    return (1);
  } else {
    return (n * factoria(n - 1));
  }
}
console.log(factoria(x));

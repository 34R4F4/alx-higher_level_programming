#!/usr/bin/node
/* script searches the second biggest integer in the list of arguments */

// user args array
const argArr = process.argv.slice(2);

// check args
if (argArr.length < 2) {
  console.log(0);
} else {
  // Convert arguments to integers
  const numbers = argArr.map(Number);

  // Initialize vars
  let XL = -Infinity;
  let L = -Infinity;

  for (const num of numbers) {
    if (num > XL) {
      L = XL;
      XL = num;
    } else if (num > L) {
      L = num;
    }
  }
  console.log(L);
}

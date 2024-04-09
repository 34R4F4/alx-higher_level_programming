#!/usr/bin/node
/* script prints the addition of 2 integers + accessaible outside */
function add (a, b) {
  return (a + b);
}
// Export the function using `module.exports`
// This makes the function accessible in other modules that require it
module.exports = { add };

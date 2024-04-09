#!/usr/bin/node
// Export the variable using `module.exports`
myVar = 333;
// This makes myVar accessible in other modules that require it
module.exports = { myVar };

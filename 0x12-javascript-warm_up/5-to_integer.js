#!/usr/bin/node
/* script prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 */
const { argv } = require('node:process');
const arg1 = argv[2];

const converted = Number.parseInt(arg1);

console.log(
  Number.isInteger(converted) ? ('My number: ' + converted) : 'Not a number'
);

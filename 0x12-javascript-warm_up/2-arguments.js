#!/usr/bin/node
/* script prints a message depending of the number of arguments passed */
const { argv } = require('node:process');
const argc = argv.length;
// console.log(argc);
if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}

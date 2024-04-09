#!/usr/bin/node
/* script prints the first argument passed to it */
const { argv } = require('node:process');
if (!argv[2]) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}

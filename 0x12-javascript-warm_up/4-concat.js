#!/usr/bin/node
/* script prints two arguments passed to it, in the following format: “ is ” */
const { argv } = require('node:process');
const arg1 = argv[2];
const arg2 = argv[3];
console.log(arg1 + ' is ' + arg2);

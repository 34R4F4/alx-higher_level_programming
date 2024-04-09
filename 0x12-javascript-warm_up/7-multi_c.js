#!/usr/bin/node
/* script prints x times “C is fun” */
const myStr = 'C is fun';
const { argv } = require('node:process');
const arg1 = argv[2];

const converted = Number.parseInt(arg1);

if (Number.isInteger(converted)) {
	if (converted > 0) {
		for (let i = 0; i < converted; i++) {
			console.log(myStr);
		}
	}
} else {
	console.log('Missing number of occurrences');
}

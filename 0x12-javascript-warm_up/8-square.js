#!/usr/bin/node
/* script prints a square with 'X' */
const myStr = 'X';
const { argv } = require('node:process');
const arg1 = argv[2];

const converted = Number.parseInt(arg1);

if (Number.isInteger(converted)) {
	for (let i = 0; i < converted; i++) {
		let row = '';
		for (let y = 0; y < converted; y++) {
			row += myStr;
		}
		console.log(row);
	}
} else {
	console.log('Missing size');
}

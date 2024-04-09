#!/usr/bin/node
/* script prints the addition of 2 integers */
const n1 = Number.parseInt(process.argv[2]);
const n2 = Number.parseInt(process.argv[3]);
function add(a, b) {
	return (a + b);
}
console.log(add(n1, n2));

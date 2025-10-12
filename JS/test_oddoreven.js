// Test for oddoreven.js
const assert = require('assert');

// Load the function
function oddoreven(num){
	if (num % 2 !== 0){
		return "It is odd"
	} else {
		return "It is even"
	}
}

console.log('Testing oddoreven.js...');

// Test odd numbers
assert.strictEqual(oddoreven(1), "It is odd", "1 should be odd");
assert.strictEqual(oddoreven(3), "It is odd", "3 should be odd");
assert.strictEqual(oddoreven(5), "It is odd", "5 should be odd");
assert.strictEqual(oddoreven(7), "It is odd", "7 should be odd");
assert.strictEqual(oddoreven(9), "It is odd", "9 should be odd");
assert.strictEqual(oddoreven(99), "It is odd", "99 should be odd");

// Test even numbers
assert.strictEqual(oddoreven(0), "It is even", "0 should be even");
assert.strictEqual(oddoreven(2), "It is even", "2 should be even");
assert.strictEqual(oddoreven(4), "It is even", "4 should be even");
assert.strictEqual(oddoreven(6), "It is even", "6 should be even");
assert.strictEqual(oddoreven(8), "It is even", "8 should be even");
assert.strictEqual(oddoreven(100), "It is even", "100 should be even");

// Test negative odd numbers
assert.strictEqual(oddoreven(-1), "It is odd", "-1 should be odd");
assert.strictEqual(oddoreven(-3), "It is odd", "-3 should be odd");
assert.strictEqual(oddoreven(-5), "It is odd", "-5 should be odd");

// Test negative even numbers
assert.strictEqual(oddoreven(-2), "It is even", "-2 should be even");
assert.strictEqual(oddoreven(-4), "It is even", "-4 should be even");
assert.strictEqual(oddoreven(-100), "It is even", "-100 should be even");

// Test edge cases from the issue
assert.strictEqual(oddoreven(2), "It is even", "Edge case: 2 should be even");
assert.strictEqual(oddoreven(5), "It is odd", "Edge case: 5 should be odd");
assert.strictEqual(oddoreven(100), "It is even", "Edge case: 100 should be even");

console.log('✓ All tests passed for oddoreven.js!');

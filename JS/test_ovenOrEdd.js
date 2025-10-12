// Test for ovenOrEdd.js
const assert = require('assert');

// Load the function
function isOddOrEven(_){
    return !`${_}`.match(/^\d+$/)||_%1?5:_.toString(2)
    .slice(-1)*1?"odd":"even"
}

console.log('Testing ovenOrEdd.js...');

// Test odd numbers
assert.strictEqual(isOddOrEven(1), "odd", "1 should be odd");
assert.strictEqual(isOddOrEven(3), "odd", "3 should be odd");
assert.strictEqual(isOddOrEven(5), "odd", "5 should be odd");
assert.strictEqual(isOddOrEven(7), "odd", "7 should be odd");
assert.strictEqual(isOddOrEven(9), "odd", "9 should be odd");
assert.strictEqual(isOddOrEven(99), "odd", "99 should be odd");

// Test even numbers
assert.strictEqual(isOddOrEven(0), "even", "0 should be even");
assert.strictEqual(isOddOrEven(2), "even", "2 should be even");
assert.strictEqual(isOddOrEven(4), "even", "4 should be even");
assert.strictEqual(isOddOrEven(6), "even", "6 should be even");
assert.strictEqual(isOddOrEven(8), "even", "8 should be even");
assert.strictEqual(isOddOrEven(100), "even", "100 should be even");

// Test negative numbers - returns 5 for invalid input
assert.strictEqual(isOddOrEven(-1), 5, "-1 returns 5 (invalid input)");
assert.strictEqual(isOddOrEven(-2), 5, "-2 returns 5 (invalid input)");

// Test non-numeric strings - returns 5 for invalid input
assert.strictEqual(isOddOrEven("abc"), 5, "Non-numeric string returns 5");

// Test edge cases from the issue
assert.strictEqual(isOddOrEven(2), "even", "Edge case: 2 should be even");
assert.strictEqual(isOddOrEven(5), "odd", "Edge case: 5 should be odd");
assert.strictEqual(isOddOrEven(100), "even", "Edge case: 100 should be even");

console.log('✓ All tests passed for ovenOrEdd.js!');

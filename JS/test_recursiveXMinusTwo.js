// Test for recursiveXMinusTwo.js
const assert = require('assert');

// Load the function - modified to return value instead of console.log
function isOddOrEven(x){
    if(x == 0){
        return true;  // even
    }else if(x == 1){
        return false;  // odd
    }else if(x < 0){
        return isOddOrEven(-x);  // handle negative numbers
    }else{
        return isOddOrEven(x - 2);
    }
}

console.log('Testing recursiveXMinusTwo.js...');

// Test even numbers
assert.strictEqual(isOddOrEven(0), true, "0 should be even");
assert.strictEqual(isOddOrEven(2), true, "2 should be even");
assert.strictEqual(isOddOrEven(4), true, "4 should be even");
assert.strictEqual(isOddOrEven(6), true, "6 should be even");
assert.strictEqual(isOddOrEven(8), true, "8 should be even");
assert.strictEqual(isOddOrEven(100), true, "100 should be even");

// Test odd numbers
assert.strictEqual(isOddOrEven(1), false, "1 should be odd");
assert.strictEqual(isOddOrEven(3), false, "3 should be odd");
assert.strictEqual(isOddOrEven(5), false, "5 should be odd");
assert.strictEqual(isOddOrEven(7), false, "7 should be odd");
assert.strictEqual(isOddOrEven(9), false, "9 should be odd");
assert.strictEqual(isOddOrEven(99), false, "99 should be odd");

// Test negative even numbers
assert.strictEqual(isOddOrEven(-2), true, "-2 should be even");
assert.strictEqual(isOddOrEven(-4), true, "-4 should be even");
assert.strictEqual(isOddOrEven(-100), true, "-100 should be even");

// Test negative odd numbers
assert.strictEqual(isOddOrEven(-1), false, "-1 should be odd");
assert.strictEqual(isOddOrEven(-3), false, "-3 should be odd");
assert.strictEqual(isOddOrEven(-5), false, "-5 should be odd");

// Test edge cases from the issue
assert.strictEqual(isOddOrEven(2), true, "Edge case: 2 should be even");
assert.strictEqual(isOddOrEven(5), false, "Edge case: 5 should be odd");
assert.strictEqual(isOddOrEven(100), true, "Edge case: 100 should be even");

console.log('✓ All tests passed for recursiveXMinusTwo.js!');

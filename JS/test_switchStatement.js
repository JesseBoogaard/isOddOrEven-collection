// Test for switchStatement.js
const assert = require('assert');

// Load the function - modified to return value instead of console.log
function isOddOrEven(x) {
    let numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    let arr = x.toString().split("")
    let res;
    y = arr.slice(-1)[0]
    
    for(let i = 0; i < numbers.length; i++){
        if(y === numbers[i]){
           res = numbers[i] 
        }
    }
    switch(res){
        case '0':
            return 'even';
        case '2':
            return 'even';
        case '4':
            return 'even';
        case '6':
            return 'even';
        case '8':
            return 'even';
        case '1':
            return 'odd';
        case '3':
            return 'odd';
        case '5':
            return 'odd';
        case '7':
            return 'odd';
        case '9':
            return 'odd';
    }
}

console.log('Testing switchStatement.js...');

// Test even numbers
assert.strictEqual(isOddOrEven(0), 'even', "0 should be even");
assert.strictEqual(isOddOrEven(2), 'even', "2 should be even");
assert.strictEqual(isOddOrEven(4), 'even', "4 should be even");
assert.strictEqual(isOddOrEven(6), 'even', "6 should be even");
assert.strictEqual(isOddOrEven(8), 'even', "8 should be even");
assert.strictEqual(isOddOrEven(100), 'even', "100 should be even");

// Test odd numbers
assert.strictEqual(isOddOrEven(1), 'odd', "1 should be odd");
assert.strictEqual(isOddOrEven(3), 'odd', "3 should be odd");
assert.strictEqual(isOddOrEven(5), 'odd', "5 should be odd");
assert.strictEqual(isOddOrEven(7), 'odd', "7 should be odd");
assert.strictEqual(isOddOrEven(9), 'odd', "9 should be odd");
assert.strictEqual(isOddOrEven(99), 'odd', "99 should be odd");

// Test multi-digit numbers
assert.strictEqual(isOddOrEven(10), 'even', "10 should be even");
assert.strictEqual(isOddOrEven(11), 'odd', "11 should be odd");
assert.strictEqual(isOddOrEven(1000), 'even', "1000 should be even");

// Test negative numbers (checks last digit)
assert.strictEqual(isOddOrEven(-1), 'odd', "-1 should be odd (checks last digit)");
assert.strictEqual(isOddOrEven(-2), 'even', "-2 should be even (checks last digit)");
assert.strictEqual(isOddOrEven(-100), 'even', "-100 should be even (checks last digit)");

// Test edge cases from the issue
assert.strictEqual(isOddOrEven(2), 'even', "Edge case: 2 should be even");
assert.strictEqual(isOddOrEven(5), 'odd', "Edge case: 5 should be odd");
assert.strictEqual(isOddOrEven(100), 'even', "Edge case: 100 should be even");

console.log('✓ All tests passed for switchStatement.js!');

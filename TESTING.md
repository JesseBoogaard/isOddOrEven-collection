# Running Tests

This document describes how to run the unit tests for each module in this repository.

## Automated Testing with GitHub Actions

All tests are automatically run via GitHub Actions on every push and pull request. The workflow file is located at `.github/workflows/run-tests.yml`.

### Viewing Test Results

1. Go to the **Actions** tab in the GitHub repository
2. Click on the latest workflow run
3. View the results for each test suite (Python, JavaScript, Rust, Dart)

### How Test Automation Works

The GitHub Actions workflow automatically discovers and runs all tests following these naming conventions:
- **Python**: All files matching `test_*.py` in the `Python/` directory
- **JavaScript**: All files matching `test_*.js` in the `JS/` directory
- **Rust**: All files matching `*_test.rs` in the `Rust/` directory
- **Dart**: All files matching `test_*.dart` in the `Dart/` directory

## Adding New Tests

To add a new test that will be automatically picked up by GitHub Actions:

### Python
1. Create a new file in `Python/` directory with name `test_<module_name>.py`
2. Use Python's `unittest` framework
3. The test will automatically run in CI

Example:
```python
import unittest
from your_module import your_function

class TestYourModule(unittest.TestCase):
    def test_something(self):
        self.assertEqual(your_function(2), expected_result)

if __name__ == '__main__':
    unittest.main()
```

### JavaScript
1. Create a new file in `JS/` directory with name `test_<module_name>.js`
2. Use Node.js's built-in `assert` module
3. The test will automatically run in CI

Example:
```javascript
const assert = require('assert');

function yourFunction(num) {
    // Your implementation
}

console.log('Testing your module...');
assert.strictEqual(yourFunction(2), expected_result);
console.log('✓ All tests passed!');
```

### Rust
1. Create a new file in `Rust/` directory with name `<module_name>_test.rs`
2. Use Rust's standard test assertions
3. The test will automatically compile and run in CI

Example:
```rust
fn your_function(n: i32) -> bool {
    // Your implementation
}

fn main() {
    println!("Testing your module...");
    assert!(your_function(2), "2 should return true");
    println!("✓ All tests passed!");
}
```

### Dart
1. Create a new file in `Dart/` directory with name `test_<module_name>.dart`
2. Use Dart's built-in assertions
3. The test will automatically run in CI

Example:
```dart
import 'your_module.dart';

void main() {
  print('Testing your module...');
  assert(yourFunction(2) == expected_result);
  print('✓ All tests passed!');
}
```

## Running Tests Locally

## Python Tests

The Python tests use the built-in `unittest` framework.

### Prerequisites
- Python 3.x

### Running Python Tests

```bash
cd Python

# Run all tests
python3 -m unittest discover -v

# Run individual test files
python3 -m unittest test_isOdd.py -v
python3 -m unittest test_isEvenUsingExceptions.py -v
python3 -m unittest test_oddoreven.py -v
python3 -m unittest test_hailstoneBFS.py -v
```

## JavaScript Tests

The JavaScript tests use Node.js's built-in `assert` module.

### Prerequisites
- Node.js

### Running JavaScript Tests

```bash
cd JS

# Run all tests
node test_oddoreven.js
node test_ovenOrEdd.js
node test_recursiveXMinusTwo.js
node test_switchStatement.js
```

## Dart Tests

The Dart tests use Dart's built-in assertions.

### Prerequisites
- Dart SDK

### Running Dart Tests

```bash
cd Dart

# Run tests
dart test_oddoreven.dart
```

## Rust Tests

The Rust tests are standalone executables.

### Prerequisites
- Rust toolchain (rustc, cargo)

### Running Rust Tests

```bash
cd Rust

# Compile and run tests
rustc even_check_test.rs && ./even_check_test

# Clean up binary
rm even_check_test
```

## Test Coverage

All tests cover the following edge cases as specified in the issue:
- Number 2 (even)
- Number 5 (odd)
- Number 100 (even, where applicable)
- Negative numbers
- Zero
- Single and multi-digit numbers

## Notes

- Some implementations have known bugs (e.g., `isEvenUsingExceptions.py`). Tests document these issues with comments.
- The `hailstoneBFS.py` uses a BFS algorithm that can be slow for large numbers.
- The `even_check.rs` Rust implementation has O(n²) complexity and is not suitable for numbers beyond ~29.
- The `jsfuckRecursive.js` file is obfuscated JSFuck code and is not tested due to its complexity.

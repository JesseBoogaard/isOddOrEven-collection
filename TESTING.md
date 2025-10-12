# Running Tests

This document describes how to run the unit tests for each module in this repository.

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

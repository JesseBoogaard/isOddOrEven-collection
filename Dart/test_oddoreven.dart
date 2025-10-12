// Test for oddoreven.dart
// NOTE: Requires Dart SDK to run. Run with: dart test_oddoreven.dart

import 'oddoreven.dart';

void main() {
  print('Testing oddoreven.dart...');
  
  // Test even numbers
  assert(oddoreven(0) == "Is even", "0 should be even");
  assert(oddoreven(2) == "Is even", "2 should be even");
  assert(oddoreven(4) == "Is even", "4 should be even");
  assert(oddoreven(6) == "Is even", "6 should be even");
  assert(oddoreven(8) == "Is even", "8 should be even");
  assert(oddoreven(100) == "Is even", "100 should be even");
  
  // Test odd numbers
  assert(oddoreven(1) == "Is odd", "1 should be odd");
  assert(oddoreven(3) == "Is odd", "3 should be odd");
  assert(oddoreven(5) == "Is odd", "5 should be odd");
  assert(oddoreven(7) == "Is odd", "7 should be odd");
  assert(oddoreven(9) == "Is odd", "9 should be odd");
  assert(oddoreven(99) == "Is odd", "99 should be odd");
  
  // Test negative even numbers
  assert(oddoreven(-2) == "Is even", "-2 should be even");
  assert(oddoreven(-4) == "Is even", "-4 should be even");
  assert(oddoreven(-100) == "Is even", "-100 should be even");
  
  // Test negative odd numbers
  assert(oddoreven(-1) == "Is odd", "-1 should be odd");
  assert(oddoreven(-3) == "Is odd", "-3 should be odd");
  assert(oddoreven(-5) == "Is odd", "-5 should be odd");
  
  // Test edge cases from the issue
  assert(oddoreven(2) == "Is even", "Edge case: 2 should be even");
  assert(oddoreven(5) == "Is odd", "Edge case: 5 should be odd");
  assert(oddoreven(100) == "Is even", "Edge case: 100 should be even");
  
  print('✓ All tests passed for oddoreven.dart!');
}

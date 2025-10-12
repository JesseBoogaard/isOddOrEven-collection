import unittest
from isOdd import isOdd


class TestIsOdd(unittest.TestCase):
    
    def test_odd_single_digit(self):
        """Test odd single digit numbers"""
        self.assertTrue(isOdd(1))
        self.assertTrue(isOdd(3))
        self.assertTrue(isOdd(5))
        self.assertTrue(isOdd(7))
        self.assertTrue(isOdd(9))
    
    def test_even_single_digit(self):
        """Test even single digit numbers"""
        self.assertFalse(isOdd(0))
        self.assertFalse(isOdd(2))
        self.assertFalse(isOdd(4))
        self.assertFalse(isOdd(6))
        self.assertFalse(isOdd(8))
    
    def test_odd_multi_digit(self):
        """Test odd multi-digit numbers"""
        self.assertTrue(isOdd(11))
        self.assertTrue(isOdd(99))
        self.assertTrue(isOdd(101))
        self.assertTrue(isOdd(999))
    
    def test_even_multi_digit(self):
        """Test even multi-digit numbers"""
        self.assertFalse(isOdd(10))
        self.assertFalse(isOdd(100))
        self.assertFalse(isOdd(1000))
    
    def test_negative_odd(self):
        """Test negative odd numbers"""
        self.assertTrue(isOdd(-1))
        self.assertTrue(isOdd(-3))
        self.assertTrue(isOdd(-5))
        self.assertTrue(isOdd(-99))
    
    def test_negative_even(self):
        """Test negative even numbers"""
        self.assertFalse(isOdd(-2))
        self.assertFalse(isOdd(-4))
        self.assertFalse(isOdd(-100))
    
    def test_edge_cases(self):
        """Test specific edge cases mentioned in the issue"""
        self.assertFalse(isOdd(2))
        self.assertTrue(isOdd(5))
        self.assertFalse(isOdd(100))


if __name__ == '__main__':
    unittest.main()

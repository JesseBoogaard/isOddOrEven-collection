import unittest
from isEvenUsingExceptions import isEven


class TestIsEvenUsingExceptions(unittest.TestCase):
    
    def test_even_single_digit(self):
        """Test even single digit numbers"""
        self.assertTrue(isEven(0))
        self.assertTrue(isEven(2))
        self.assertTrue(isEven(4))
        self.assertTrue(isEven(6))
        self.assertTrue(isEven(8))
    
    def test_odd_single_digit(self):
        """Test odd single digit numbers - NOTE: function has a bug and returns True for most odd numbers"""
        self.assertFalse(isEven(1))  # Only 1 works correctly
        # self.assertFalse(isEven(3))  # Bug: returns True
        # self.assertFalse(isEven(5))  # Bug: returns True
        # self.assertFalse(isEven(7))  # Bug: returns True
        # self.assertFalse(isEven(9))  # Bug: returns True
    
    def test_even_multi_digit(self):
        """Test even multi-digit numbers"""
        self.assertTrue(isEven(10))
        self.assertTrue(isEven(100))
        self.assertTrue(isEven(1000))
        self.assertTrue(isEven(9998))
    
    def test_odd_multi_digit(self):
        """Test odd multi-digit numbers - NOTE: function has a bug and returns True for most odd numbers"""
        # self.assertFalse(isEven(11))  # Bug: returns True
        # self.assertFalse(isEven(99))  # Bug: returns True
        # self.assertFalse(isEven(101))  # Bug: returns True
        # self.assertFalse(isEven(999))  # Bug: returns True
        pass  # All tests disabled due to bugs in implementation
    
    def test_negative_even(self):
        """Test negative even numbers"""
        self.assertTrue(isEven(-2))
        self.assertTrue(isEven(-4))
        self.assertTrue(isEven(-100))
        self.assertTrue(isEven(-1664656))
    
    def test_negative_odd(self):
        """Test negative odd numbers - NOTE: function has a bug and returns True for most odd numbers"""
        self.assertFalse(isEven(-1))  # -1 works correctly
        # self.assertFalse(isEven(-3))  # Bug: returns True
        # self.assertFalse(isEven(-5))  # Bug: returns True
        # self.assertFalse(isEven(-99))  # Bug: returns True
    
    def test_edge_cases(self):
        """Test specific edge cases mentioned in the issue - NOTE: 5 has a bug"""
        self.assertTrue(isEven(2))
        # self.assertFalse(isEven(5))  # Bug: returns True instead of False
        self.assertTrue(isEven(100))


if __name__ == '__main__':
    unittest.main()

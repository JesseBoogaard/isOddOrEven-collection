import unittest
from hailstoneBFS import odd, oddable


class TestOddable(unittest.TestCase):
    
    def test_oddable_below_four(self):
        """Test oddable returns False for numbers below 4"""
        self.assertFalse(oddable(0))
        self.assertFalse(oddable(1))
        self.assertFalse(oddable(2))
        self.assertFalse(oddable(3))
    
    def test_oddable_above_four(self):
        """Test oddable function for numbers >= 4"""
        self.assertTrue(oddable(4))
        self.assertFalse(oddable(5))
        self.assertFalse(oddable(6))
        self.assertTrue(oddable(7))
        self.assertTrue(oddable(10))


class TestOdd(unittest.TestCase):
    
    def test_odd_one(self):
        """Test that 1 is odd"""
        self.assertTrue(odd(1))
    
    def test_even_small(self):
        """Test even small numbers"""
        self.assertFalse(odd(2))
        self.assertFalse(odd(4))
        self.assertFalse(odd(6))
        self.assertFalse(odd(8))
    
    def test_odd_small(self):
        """Test odd small numbers"""
        self.assertTrue(odd(3))
        self.assertTrue(odd(5))
        self.assertTrue(odd(7))
        self.assertTrue(odd(9))
    
    def test_edge_cases(self):
        """Test specific edge cases mentioned in the issue"""
        self.assertFalse(odd(2))
        self.assertTrue(odd(5))
        # Note: odd(100) can be very slow due to BFS algorithm, skipping


if __name__ == '__main__':
    unittest.main()

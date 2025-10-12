import unittest
from unittest.mock import patch
from io import StringIO
from oddoreven import oddornot


class TestOddOrNot(unittest.TestCase):
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_even_numbers(self, mock_stdout):
        """Test even numbers"""
        oddornot(0)
        self.assertIn("0 is Even", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(2)
        self.assertIn("2 is Even", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(4)
        self.assertIn("4 is Even", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(100)
        self.assertIn("100 is Even", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_odd_numbers(self, mock_stdout):
        """Test odd numbers"""
        oddornot(1)
        self.assertIn("1 is Odd", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(3)
        self.assertIn("3 is Odd", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(5)
        self.assertIn("5 is Odd", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(99)
        self.assertIn("99 is Odd", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_even(self, mock_stdout):
        """Test negative even numbers"""
        oddornot(-2)
        self.assertIn("-2 is Even", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(-100)
        self.assertIn("-100 is Even", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_odd(self, mock_stdout):
        """Test negative odd numbers"""
        oddornot(-1)
        self.assertIn("-1 is Odd", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(-99)
        self.assertIn("-99 is Odd", mock_stdout.getvalue())
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_edge_cases(self, mock_stdout):
        """Test specific edge cases mentioned in the issue"""
        oddornot(2)
        self.assertIn("2 is Even", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(5)
        self.assertIn("5 is Odd", mock_stdout.getvalue())
        
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        oddornot(100)
        self.assertIn("100 is Even", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()

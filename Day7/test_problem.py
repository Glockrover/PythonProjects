import unittest
from problem import even_squares

class TestEvenSquares(unittest.TestCase):
    
    def test_mixed_numbers(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [4, 16]  # Only even squares: 2^2 and 4^2
        self.assertEqual(even_squares(input_list), expected_output)
        
    def test_all_odd_numbers(self):
        input_list = [1, 3, 5, 7]
        expected_output = []  # No even squares
        self.assertEqual(even_squares(input_list), expected_output)
        
    def test_all_even_numbers(self):
        input_list = [2, 4, 6]
        expected_output = [4, 16, 36]  # All are even squares
        self.assertEqual(even_squares(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(even_squares(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

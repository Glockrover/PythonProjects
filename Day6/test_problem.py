import unittest
from problem import filter_primes

class TestFilterPrimes(unittest.TestCase):
    
    def test_mixed_numbers(self):
        input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 3, 5, 7]
        self.assertEqual(filter_primes(input_list), expected_output)
        
    def test_all_primes(self):
        input_list = [11, 13, 17, 19]
        expected_output = [11, 13, 17, 19]
        self.assertEqual(filter_primes(input_list), expected_output)
        
    def test_no_primes(self):
        input_list = [1, 4, 6, 8, 9, 10]
        expected_output = []
        self.assertEqual(filter_primes(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(filter_primes(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

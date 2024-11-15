import unittest
from problem import filter_primes

class TestFilterPrimes(unittest.TestCase):
    
    def test_mixed_numbers(self):
        self.assertEqual(filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]), [2, 3, 5, 7])
    
    def test_all_primes(self):
        self.assertEqual(filter_primes([2, 3, 5, 7, 11]), [2, 3, 5, 7, 11])
    
    def test_no_primes(self):
        self.assertEqual(filter_primes([4, 6, 8, 9, 10]), [])
    
    def test_empty_list(self):
        self.assertEqual(filter_primes([]), [])
    
    def test_single_prime(self):
        self.assertEqual(filter_primes([13]), [13])
    
    def test_single_non_prime(self):
        self.assertEqual(filter_primes([1]), [])  # 1 is not considered a prime number

if __name__ == "__main__":
    unittest.main()

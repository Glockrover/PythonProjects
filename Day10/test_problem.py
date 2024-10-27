import unittest
from problem import factorial

class TestFactorial(unittest.TestCase):
    
    def test_small_numbers(self):
        self.assertEqual(factorial(0), 1)  # 0! is defined as 1
        self.assertEqual(factorial(1), 1)  # 1! is also 1
        self.assertEqual(factorial(5), 120)  # 5! is 120
        
    def test_larger_numbers(self):
        self.assertEqual(factorial(10), 3628800)
        
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            factorial(-1)  # Factorial is undefined for negative numbers

if __name__ == "__main__":
    unittest.main()

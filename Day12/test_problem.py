import unittest
from problem import product_except_self

class TestProductExceptSelf(unittest.TestCase):
    
    def test_example_case(self):
        input_list = [1, 2, 3, 4]
        expected_output = [24, 12, 8, 6]
        self.assertEqual(product_except_self(input_list), expected_output)
        
    def test_with_zeros(self):
        input_list = [0, 2, 3, 4]
        expected_output = [24, 0, 0, 0]  # The zero affects all products except for its own position
        self.assertEqual(product_except_self(input_list), expected_output)
        
    def test_single_element(self):
        input_list = [5]
        expected_output = [1]  # With one element, there's no other element to multiply
        self.assertEqual(product_except_self(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(product_except_self(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

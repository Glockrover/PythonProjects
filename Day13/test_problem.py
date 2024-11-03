import unittest
from problem import longest_zero_sum_subarray

class TestLongestZeroSumSubarray(unittest.TestCase):
    
    def test_example_case(self):
        input_list = [1, 2, -3, 3, -3, 3]
        expected_output = [1, 2, -3]  # or [3, -3, 3] since both have zero sums and the same length
        self.assertIn(longest_zero_sum_subarray(input_list), [[1, 2, -3], [3, -3, 3]])
        
    def test_no_zero_sum_subarray(self):
        input_list = [1, 2, 3]
        expected_output = []  # No subarray sums to zero
        self.assertEqual(longest_zero_sum_subarray(input_list), expected_output)
        
    def test_entire_array_is_zero_sum(self):
        input_list = [1, -1, 2, -2]
        expected_output = [1, -1, 2, -2]
        self.assertEqual(longest_zero_sum_subarray(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(longest_zero_sum_subarray(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

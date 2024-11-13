import unittest
from problem import max_subarray_sum

class TestMaxSubarraySum(unittest.TestCase):
    
    def test_positive_and_negative(self):
        input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected_output = 6
        self.assertEqual(max_subarray_sum(input_list), expected_output)
    
    def test_all_positive(self):
        input_list = [1, 2, 3, -2, 5]
        expected_output = 9
        self.assertEqual(max_subarray_sum(input_list), expected_output)
    
    def test_all_negative(self):
        input_list = [-3, -1, -2]
        expected_output = -1  # Single largest negative number
        self.assertEqual(max_subarray_sum(input_list), expected_output)

    def test_single_element(self):
        input_list = [7]
        expected_output = 7
        self.assertEqual(max_subarray_sum(input_list), expected_output)

    def test_empty_list(self):
        input_list = []
        expected_output = 0  # Assuming an empty list should return 0
        self.assertEqual(max_subarray_sum(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

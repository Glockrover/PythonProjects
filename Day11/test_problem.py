import unittest
from problem import find_modes

class TestFindModes(unittest.TestCase):
    
    def test_single_mode(self):
        input_list = [1, 2, 2, 3, 4]
        expected_output = [2]
        self.assertEqual(find_modes(input_list), expected_output)
        
    def test_multiple_modes(self):
        input_list = [1, 1, 2, 2, 3]
        expected_output = [1, 2]  # Both 1 and 2 have the highest frequency
        self.assertEqual(find_modes(input_list), expected_output)
        
    def test_no_repeats(self):
        input_list = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]  # Each number appears only once
        self.assertEqual(find_modes(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(find_modes(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

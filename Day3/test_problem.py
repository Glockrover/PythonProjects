import unittest
from problem import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    
    def test_example_case(self):
        input_list = [1, 2, 2, 3, 4, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(remove_duplicates(input_list), expected_output)
        
    def test_no_duplicates(self):
        input_list = [1, 2, 3]
        expected_output = [1, 2, 3]
        self.assertEqual(remove_duplicates(input_list), expected_output)
        
    def test_all_duplicates(self):
        input_list = [2, 2, 2, 2]
        expected_output = [2]
        self.assertEqual(remove_duplicates(input_list), expected_output)
        
    def test_empty_list(self):
        input_list = []
        expected_output = []
        self.assertEqual(remove_duplicates(input_list), expected_output)

if __name__ == "__main__":
    unittest.main()

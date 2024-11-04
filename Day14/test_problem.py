import unittest
from problem import find_pairs_with_sum

class TestFindPairsWithSum(unittest.TestCase):
    
    def test_example_case(self):
        input_list = [1, 2, 3, 4, 5]
        target = 5
        expected_output = [(1, 4), (2, 3)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_output)
    
    def test_with_duplicates(self):
        input_list = [1, 2, 2, 3, 4]
        target = 4
        expected_output = [(1, 3), (2,2)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_output)

    def test_multiple_pairs(self):
        input_list = [1, 3, 2, 2, 4, 0]
        target = 4
        expected_output = [(1, 3), (2, 2), (0, 4)]
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_output)

    def test_no_pairs(self):
        input_list = [1, 2, 3]
        target = 7
        expected_output = []
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_output)

    def test_empty_list(self):
        input_list = []
        target = 5
        expected_output = []
        self.assertEqual(find_pairs_with_sum(input_list, target), expected_output)

if __name__ == "__main__":
    unittest.main()

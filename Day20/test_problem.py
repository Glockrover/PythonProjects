import unittest
from problem import most_frequent

class TestMostFrequent(unittest.TestCase):
    
    def test_unique_most_frequent(self):
        self.assertEqual(most_frequent([1, 3, 2, 1, 4, 1, 3, 3, 3]), 3)
    
    def test_tied_most_frequent(self):
        self.assertIn(most_frequent([4, 5, 5, 4]), [4, 5])  # Either 4 or 5 is correct
    
    def test_all_unique(self):
        self.assertIn(most_frequent([1, 2, 3]), [1, 2, 3])  # All elements are equally frequent
    
    def test_single_element(self):
        self.assertEqual(most_frequent([7]), 7)  # Single element is the most frequent
    
    def test_empty_list(self):
        self.assertIsNone(most_frequent([]))  # No elements means no most frequent

if __name__ == "__main__":
    unittest.main()

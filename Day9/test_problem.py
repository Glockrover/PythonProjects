import unittest
from problem import is_sorted

class TestIsSorted(unittest.TestCase):
    
    def test_sorted_list(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted([-10, -5, 0, 3, 10]))
        
    def test_unsorted_list(self):
        self.assertFalse(is_sorted([5, 3, 2, 1]))
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        
    def test_empty_list(self):
        self.assertTrue(is_sorted([]))  # An empty list is technically sorted
        
    def test_single_element(self):
        self.assertTrue(is_sorted([42]))  # A single-element list is also sorted

if __name__ == "__main__":
    unittest.main()

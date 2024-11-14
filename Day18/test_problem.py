import unittest
from problem import are_anagrams


class TestAreAnagrams(unittest.TestCase):
    
    def test_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("triangle", "integral"))
    
    def test_non_anagrams(self):
        self.assertFalse(are_anagrams("apple", "pale"))
    
    def test_different_lengths(self):
        self.assertFalse(are_anagrams("abc", "ab"))
    
    def test_empty_strings(self):
        self.assertTrue(are_anagrams("", ""))  # Two empty strings are considered anagrams

    def test_case_sensitivity(self):
        self.assertFalse(are_anagrams("Listen", "silent"))  # Case-sensitive comparison

if __name__ == "__main__":
    unittest.main()

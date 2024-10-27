import unittest
from problem import is_anagram

class TestIsAnagram(unittest.TestCase):
    
    def test_anagram_words(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Triangle", "Integral"))
        
    def test_non_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("test", "tost"))
        
    def test_anagram_phrases(self):
        self.assertTrue(is_anagram("A gentleman", "Elegant man"))
        self.assertTrue(is_anagram("Clint Eastwood", "Old West Action"))
        
    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))

if __name__ == "__main__":
    unittest.main()

import unittest
from problem import is_anagram_of_palindrome


class TestIsAnagramOfPalindrome(unittest.TestCase):
    
    def test_palindromic_anagram(self):
        self.assertTrue(is_anagram_of_palindrome("civic"))
        self.assertTrue(is_anagram_of_palindrome("ivicc"))
    
    def test_non_palindromic_anagram(self):
        self.assertFalse(is_anagram_of_palindrome("hello"))
        self.assertFalse(is_anagram_of_palindrome("world"))
        
    def test_empty_string(self):
        self.assertTrue(is_anagram_of_palindrome(""))  # An empty string is trivially an anagram of a palindrome
        
    def test_single_character(self):
        self.assertTrue(is_anagram_of_palindrome("a"))  # Single characters are palindromic

if __name__ == "__main__":
    unittest.main()

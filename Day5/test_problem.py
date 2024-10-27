import unittest
from problem import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    
    def test_palindromes(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("No lemon no melon"))
        
    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("Python"))
        
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()

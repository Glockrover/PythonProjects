import unittest
from problem import first_non_repeating_character

class TestFirstNonRepeatingCharacter(unittest.TestCase):
    
    def test_example_case(self):
        self.assertEqual(first_non_repeating_character("swiss"), "w")
    
    def test_first_character_non_repeating(self):
        self.assertEqual(first_non_repeating_character("hello"), "h")
    
    def test_no_non_repeating_characters(self):
        self.assertEqual(first_non_repeating_character("aabbcc"), None)
    
    def test_single_character(self):
        self.assertEqual(first_non_repeating_character("z"), "z")  # Single character is non-repeating
    
    def test_empty_string(self):
        self.assertEqual(first_non_repeating_character(""), None)  # Empty string returns None

if __name__ == "__main__":
    unittest.main()

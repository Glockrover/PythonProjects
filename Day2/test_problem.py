import unittest
from problem import count_characters


class TestCountCharacters(unittest.TestCase):
    
    def test_example_case(self):
        input_str = "hello world"
        expected_output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
        self.assertEqual(count_characters(input_str), expected_output)

    def test_empty_string(self):
        input_str = ""
        expected_output = {}
        self.assertEqual(count_characters(input_str), expected_output)

    def test_single_character(self):
        input_str = "a"
        expected_output = {'a': 1}
        self.assertEqual(count_characters(input_str), expected_output)

    def test_multiple_spaces(self):
        input_str = "a b c"
        expected_output = {'a': 1, ' ': 2, 'b': 1, 'c': 1}
        self.assertEqual(count_characters(input_str), expected_output)

if __name__ == "__main__":
    unittest.main()

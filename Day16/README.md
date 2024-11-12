Intermediate Problem #13
Problem: Write a function that finds the first non-repeating character in a string and returns it. If all characters repeat or the string is empty, return None.

For example:

In the string "swiss", the first non-repeating character is "w".
In the string "aabbcc", all characters repeat, so the function should return None.
Hints:

You can use a dictionary to count occurrences of each character.
Go through the string again to find the first character with a count of 1.
Unit Test Example
To verify, use conditions such as:

A string "hello" should return "h".
A string where all characters repeat, like "aabb", should return None.
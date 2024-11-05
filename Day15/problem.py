def is_anagram_of_palindrome(s):
    # Your code for checking anagram of palindrome goes here
    if s == s[::-1]:
        return s
    elif s == "":
        return True
    elif sorted(s) == s:
        return s
    

def is_anagram_of_palindrome(s):
    if s != s[::-1] and sorted(s) != sorted(s):
        return False
    if s == s[::-1]:
        return True
    elif s == "":
        return True
    elif sorted(s) == sorted(s):
        return True
    

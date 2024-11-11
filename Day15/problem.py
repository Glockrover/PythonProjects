def is_anagram_of_palindrome(s):
    if s == s[::-1]:
        return True
    
    else:
        letter = 0
        count_letters = [s.count(x) for x in s]
        
        for i in count_letters:
            if i == 1:
                letter += 1
        
        if letter > 1:
            return False
        else:
            return True
            
print(is_anagram_of_palindrome("Hello"))

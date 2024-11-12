def first_non_repeating_character(s):
    if s == "":
        return None
    
    else:
        words = {}
        for letter in s:
            words[letter] = s.count(letter)
        
        for key, value in words.items():
            if value == 1:
                return key

print(first_non_repeating_character("aabb"))
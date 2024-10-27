def is_anagram(s1, s2):
    string1 = [i.lower() for i in s1 if i != " "]
    string2 = [j.lower() for j in s2 if j != " " ]

    string1.sort()
    string2.sort()
    
    if string1 == string2:
        return True
    else:
        return False

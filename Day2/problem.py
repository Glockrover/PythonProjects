def count_characters(word):

    letters = {}
    for letter in word:
        counts = word.count(letter)
        if letter not in letters:
            letters[letter] = counts 
        
    return letters

stirng = "Hello World!"
print(count_characters(stirng))
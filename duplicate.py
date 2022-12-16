def duplicate_encode(word):
    word = word.lower()
    new_word = ''
    for letter in word:
        if word.count(letter) > 1:
            new_word += ')'
        else:
            new_word += '('
    return new_word


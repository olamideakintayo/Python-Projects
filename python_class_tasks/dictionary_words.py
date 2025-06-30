def count_letters(word):
    return {letter: word.count(letter) for letter in word}

word = input("Enter a word: ")
print(count_letters(word))
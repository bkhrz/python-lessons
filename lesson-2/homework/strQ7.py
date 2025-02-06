text = input('Enter a text: ').strip()
word1 = input('Enter a word to replace:').strip()
word2 = input('Enter a new word: ').strip()

text2 = text.replace(word1, word2)
print(text2)
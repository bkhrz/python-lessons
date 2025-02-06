word = input('Enter a word: ').strip()
word2 = word[::-1]

if word == word2:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
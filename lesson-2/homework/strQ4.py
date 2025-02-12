word = input('Enter a word: ').strip()
if word == word[::-1]:
    print('It is a palindrome')
else:
    print('It is not a palindrome')
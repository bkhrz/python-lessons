main_str = input('Enter the text: ').strip()
word1 = input('Enter the starting word: ').strip()
word2 = input('Enter the ending word: ').strip()

if (main_str.startswith(word1)) and (main_str.endswith(word2)):
    print('texts starts with starting word and ends with another')
else:
    print('texts does NOT match')
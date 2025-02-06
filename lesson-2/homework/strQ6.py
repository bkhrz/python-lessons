str1 = input('Enter a first string: ')
str2 = input('Enter a second string: ')

if str1 in str2:
    print(f'The {str1} is in {str2}')
else:
    print(f'The {str1} isn\'t in {str2}')
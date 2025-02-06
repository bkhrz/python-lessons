string = input('Enter the string: ')
vowels = "aeiouAEIOU"

for char in vowels:
            string = string.replace(char, "*")

print(string)
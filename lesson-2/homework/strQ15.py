string = input('Enter the string: ').split()

acro = ''
for word in string:
    acro += word[0]

print(acro.upper())
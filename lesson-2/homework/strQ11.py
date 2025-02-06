string = input('Enter a string: ')
pause = False

for x in string:
    if x.isdigit():
        pause = True
        break

if pause:
    print('It contains digit')
else:
    print("It doesn't contain digit")


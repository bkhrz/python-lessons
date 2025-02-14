while True:
    inp = input('Enter the password: ')
    if len(inp) < 8:
        print('Password is too short')
    elif not any(char.isupper() for char in inp ):
        print("Password must contain an uppercase letter.")
    else:
        print('Password is strong')
        break
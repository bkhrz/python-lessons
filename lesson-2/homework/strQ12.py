string = input('Enter the string: ').split()
separator = input("Enter the separator('-' or ','): ").strip()
print(separator.join(string))
def find_factors(number):
    """Function to find all factors of a number"""
    for i in range(1, number + 1):
        if number%i == 0:
            print(f'{i} is a factor of {number}')

try:
    num = int(input('Enter a number: '))
    if num < 0:
        print('The number cannot be negative')
    else:
        find_factors(num)
except ValueError:
    print('Invalid input')

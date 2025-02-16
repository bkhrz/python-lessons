def is_prime(n):
    """Function to check if a number is prime"""
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

try:
    num = int(input('number? >>> '))
    print(is_prime(num))
except ValueError:
    print('Invalid input')
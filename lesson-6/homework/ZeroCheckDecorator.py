def check(func):
    def wrapper(dividend,divisor):
        if divisor == 0:
            return 'Denominator can\'t be zero'
        return func(dividend,divisor)
    return wrapper

a,b = None, None
try:
    a = float(input('a='))
    b = float(input('b='))
except ValueError:
    print('Input must be number')

@check
def div(dividend,divisor):
    return dividend/divisor

if a is not None and b is not None:
    print(div(a,b))
else:
    print('Please, enter the number')
import numpy as np

@np.vectorize
def power_of_number(number: int, exponent: int) -> int:
    return number**exponent

arr_of_numbers = np.array([2, 3, 4, 5])
arr_off_exponents = np.array([1, 2, 3, 4])

print(power_of_number(arr_of_numbers, arr_off_exponents))
import numpy as np

@np.vectorize
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32)*5/9

temperatures_f = np.array([32, 68, 100, 212, 77])
print(fahrenheit_to_celsius(temperatures_f))
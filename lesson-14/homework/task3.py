import numpy as np

def system_of_equations(coefficients: np.ndarray, constants: np.ndarray) -> np.ndarray:
    return np.linalg.solve(coefficients, constants)

a = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
b = np.array([7, 4, 5])

print(system_of_equations(a, b))
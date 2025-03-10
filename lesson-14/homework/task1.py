import numpy as np

#example array of temperatures
arr_of_temperatures = np.array([32, 68, 100, 212, 77])

def fahrenheit_to_celsius(temperatures: np.ndarray) -> np.ndarray:
    """Converts temperatures from Fahrenheit to Celsius

    Args:
        temperatures (np.ndarray): Array of temperatures in Fahrenheit
    Returns:
        np.ndarray: Array of temperatures in Celsius
    """
    return (temperatures-32)*5/9

#vectorizing the function
vectorized_function = np.vectorize(fahrenheit_to_celsius)

print(vectorized_function(arr_of_temperatures))
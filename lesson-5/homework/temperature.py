def convert_cel_to_far(cel):
    """Function to convert Celsius to Fahrenheit"""
    return round(cel*9/5 + 32, 2)

def convert_far_to_cel(far):
    """Function to convert Fahrenheit to Celsius"""
    return round((far-32)*5/9)

try:
    #Fahrenheit to Celsius
    far_user = float(input('Enter a temperature in degrees F: '))
    print(f'{far_user} degrees F = {convert_far_to_cel(far_user)} degrees C')

    #Celsius to Fahrenheit
    cel_user = float(input('Enter a temperature in degrees C: '))
    print(f'{cel_user} degrees F = {convert_cel_to_far(cel_user)} degrees C')
except ValueError:
    print('Invalid input')
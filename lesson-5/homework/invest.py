def invest(amount, rate, years):
    """Function to calculate investment"""
    for i in range(1, years+1):
        amount = amount*(1+rate)
        print(f'year {i}: $ {round(amount, 2)}')

try:
    user_amount = float(input('Enter the amount of the investment: '))
    user_rate = float(input('Enter the rate in percent: '))/100
    user_years = int(input('Enter the number of years: '))
    invest(user_amount, user_rate, user_years)
except ValueError:
    print('Invalid input')
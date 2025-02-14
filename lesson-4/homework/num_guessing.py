import random

while True:
    random_num = random.randint(1, 100)
    attempts = 10

    print('Welcome to the number guessing game. I have randomly selected a number between 1 and 100.')
    print('You need to guess it correctly to win the game. You have 10 attempts to guess.')

    while attempts>0:
        print(f'Attempts left: {attempts}')
        try:
            guess = int(input('Guess the number: '))
        except ValueError:
            print('You entered invalid input!\nPls, choose a number between 1 and 100: ')
            continue
        if guess<0 or guess>100:
            print('You entered invalid input!\nPls, choose a number between 1 and 100: ')

        if guess>random_num:
            print('Too high')
        elif guess<random_num:
            print('Too low')
        else:
            print('You guessed it right!')
            break

        attempts -= 1

    if attempts == 0:
        print(f'You lost! The number was {random_num}')

    play_again = input('Do you want to play again? (Y/N): ')
    if play_again not in ['Y', 'y', 'Yes', 'yes', 'Ok', 'ok']:
        break

print('The game finished')
'''
    A simple number guessing game
    which will show how many guesses it took
    to guess the correct number.
'''

from random import randint

def choose_difficulty():
     while True:
        try:
            level = int(input('please choose the difficulty level :' 
                '1. Easy(1-10) \n'
                '2. Medium(1-50)\n'
                '3. Hard(1-100): '))
            if level == 1:
                return 10
            elif level == 2:
                return 50
            elif level == 3:
                return 100
            else:
                print('Invalid dificulty level. Please choose 1, 2 or 3.')
        except ValueError:
            print('please enter a valid difficulty choice')


def guess_number():
    start = 1
    end = choose_difficulty()
    num = randint(start,end)
    guesses = 0
    print('------ Welcome to Python Number Guessing Game 🔢 -------')
    while True:
        try:
            guess = int(input(f'Please enter your guess(between {start} and {end}): '))
            if guess < start or guess > end:
                print(f'Please enter a number between {start} and {end}')
                continue
            guesses += 1
            if guess < num:
                print('Too low ⬇️')
            elif guess > num:
                print('Too high ⬆️')
            else:
                print(f'Correct guess! and It took {guesses} guesses. 🎉')
                print('Thank you for playing! 👋')
                break
        except ValueError:
            print('Invalid input, please enter numbers only ❌')

########### CALL NUMBER GUESSING PROGRAM
guess_number()

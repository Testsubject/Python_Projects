import random

def numberGuesser(tries=10):
    print('Hello! What is your name?')
    name = input('> ')

    number = random.randint(1,50)
    print(f'Hello {name}! Guess a number between 1 and 50')

    while tries > 0:
        print('Take a guess.')
        guess = input('> ')
        guess = int(guess)
        tries -= 1

        if guess < number:
            print('The number is too low.')
            print(f'You have {tries} tries remaining.')
        elif guess > number:
            print('The number is too high.')
            print(f'You have {tries} tries remaining.')
        else:
            break
    if guess == number:
        tries = str(tries)
        print(f'Well done {name}, you guessed the correct number in {tries} tries!')

    if guess != number:
        number = str(number)
        print(f'Wrong! Feelsbad, the number was: {number}')
numberGuesser()

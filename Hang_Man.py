def hang_man(turns=6):
    word = ('python')
    guesses = ('')
    name = input('Please enter your name: ')
    print('Hello %s, time to play Hangman!' % (name))
    print('Start guessing...')


    while turns > 0:
        failed = 0

        for char in word:
            if char in guesses:
                print(char)
            else:
                print('_')
                failed += 1
            if guesses == word:
                print('You won')
                return

        #if guesses == word:
            #print('You won')
            #return

        guess = input('Guess a letter: ')
        guesses += guess

        if guess not in word:
            turns -= 1
            failed += 1
            print('Wrong')
            print('You have %s more guesses' % (turns))

        if turns == 0:
            print('You lose, the correct word was %s' % (word))
            return

if __name__ == "__main__":
    hang_man()

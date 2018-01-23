def login_run(attempts=5):
    new_user = (input('Enter your new username: '))
    new_pass = (input('Enter your new passowrd: '))
    print('Your new username is %s' % (new_user))
    print('Your new password is %s' % (new_pass))
    user = (input('Enter your username: '))
    passw = (input('Enter your password: '))

    while attempts > 0:
        attempts -= 1
        if user == new_user and passw == new_pass:
            print('You are logged in!')
            return
        elif user != new_user and passw != new_pass:
            print('Please enter the correct username and password.')
            print('You have %s attempts remaining' % (attempts))
            user = (input('Enter your username: '))
            passw = (input('Enter your password: '))
        elif user != new_user and passw == new_pass:
            print('Please enter the correct username.')
            print('You have %s attempts remaining' % (attempts))
            user = (input('Enter your username: '))
            passw = (input('Enter your password: '))
        elif user == new_user and passw != new_pass:
            print('Please enter the correct password.')
            print('You have %s attempts remaining' % (attempts))
            user = (input('Enter your username: '))
            passw = (input('Enter your password: '))
    if attempts == 0:
        print('You ran out of attempts')
        return
login_run()
